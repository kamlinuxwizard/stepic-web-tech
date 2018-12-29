from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, related_name='likes')

    objects = QuestionManager()

    def __unicode__(self):
        return self.title()

    # def get_absolute_url(self):
    #     return '/question/%d/' % self.pk

    class Meta:
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.text()

    class Meta:
        ordering = ['-added_at']
