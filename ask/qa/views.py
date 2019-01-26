from django.views.decorators.http import require_GET

from django.core.paginator import Paginator, EmptyPage

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.edit import FormView
from django.views.generic.base import View

from .models import Question, Answer
from .forms import AskForm, AnswerForm, SignUpForm


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


@require_GET
def index(request):
    new_questions = Question.objects.new()

    page = paginate(request, new_questions)

    return render(request,
                  'index.html',
                  {'questions': page.object_list, 'paginator': page.paginator, 'page': page})


@require_GET
def popular(request):
    popular_questions = Question.objects.popular()

    page = paginate(request, popular_questions)

    return render(request,
                  'popular.html',
                  {'questions': page.object_list, 'paginator': page.paginator, 'page': page})


def question(request, slug):
    question = get_object_or_404(Question, id=slug)

    try:
        answers = question.answer_set.all()
    except Answer.DoesNotExist:
        answers = None

    if request.method == "POST":
        # form = AnswerForm(question, request.POST)
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            url = answer.question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        # form = AnswerForm(question)
        form = AnswerForm(initial={'question': question, })

    return render(request,
                  'question_details.html',
                  {'question': question, 'answers': answers, 'form': form})


@login_required(login_url='login')
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request,
                  'question_add.html',
                  {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()

    return render(request,
                  'signup.html',
                  {'form': form})


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "login.html"

    # Ссылка, на которую будет перенаправляться пользователь в случае успешного входа.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        # Выполняем аутентификацию пользователя.
        login(self.request, form.get_user())
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


def test(request):
    return HttpResponse('OK')
