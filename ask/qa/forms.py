from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer


class AddQuestionForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = User.objects.get(pk=1)
        question.save()
        return question


class AddAnswerForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        self.question = question
        super(AddAnswerForm, self).__init__(*args, **kwargs)

    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author = User.objects.get(pk=1)
        answer.question = self.question
        answer.save()
        return answer
