from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    _user = None

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self._user
        question.save()
        return question


class AnswerForm(forms.Form):
    """
    Вопрос подстовляется в форму через инициализацию
    """
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.filter(), initial=0)
    _user = None

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        # answer.author = User.objects.get(pk=1)
        answer.author = self._user
        answer.save()
        return answer

# class AnswerForm(forms.Form):
#     """
#     Вопрос передается в конструктор через параметры
#     """
#     def __init__(self, question, *args, **kwargs):
#         self.question = question
#         super(AnswerForm, self).__init__(*args, **kwargs)
#
#     text = forms.CharField(widget=forms.Textarea)
#
#     def clean(self):
#         return self.cleaned_data
#
#     def save(self):
#         answer = Answer(**self.cleaned_data)
#         answer.author = User.objects.get(pk=1)
#         answer.question = self.question
#         answer.save()
#         return answer


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Enter your email address.')
    # password = forms.PasswordInput()
    # password1 = None
    password2 = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

