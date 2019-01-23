from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404

from .models import Question, Answer
from .forms import AskForm, AnswerForm


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

    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page
    })


@require_GET
def popular(request):
    popular_questions = Question.objects.popular()

    page = paginate(request, popular_questions)

    return render(request, 'popular.html', {
        'questions': page.object_list,
        'paginator': page.paginator,
        'page': page
    })


def question(request, slug):
    question = get_object_or_404(Question, id=slug)

    try:
        answers = question.answer_set.all()
    except Answer.DoesNotExist:
        answers = None

    if request.method == "POST":
        form = AnswerForm(question, request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(question)

    return render(request, 'question_details.html', {
        'question': question,
        'answers': answers,
        'form': form
    })


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request,
                  'question_add.html',
                  {'form': form})


def test(request):
    return HttpResponse('OK')
