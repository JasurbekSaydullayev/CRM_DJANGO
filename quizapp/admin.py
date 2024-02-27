from django.contrib import admin

from .models import Question, Subject, Answer


@admin.register(Subject)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['text', 'is_right']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'subject_name']
    list_display = ['question_text', 'subject_name', ]
    inlines = [AnswerInlineModel]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'is_right', 'question']

