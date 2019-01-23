from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = User.objects.get(pk=1)
        question.save()
        return question


class AnswerForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        self.question = question
        super(AnswerForm, self).__init__(*args, **kwargs)

    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author = User.objects.get(pk=1)
        answer.question = self.question
        answer.save()
        return answer
