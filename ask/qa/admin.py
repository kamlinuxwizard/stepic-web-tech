from django.contrib import admin

# Register your models here.
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'added_at', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('added_at', )
    search_fields = ('title', 'text', 'author__username')
    list_per_page = 15


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'added_at', 'author')
    list_display_links = ('id', 'short_text')
    list_filter = ('added_at', )
    search_fields = ('text', 'author__username')
    list_per_page = 15
