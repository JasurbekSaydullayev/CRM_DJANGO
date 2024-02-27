from django.contrib.auth import get_user_model
from django.db import models

from .validators import validate_difficulty_question

User = get_user_model()


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubjectCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    subject = models.ForeignKey(Subject, to_field="name",
                                on_delete=models.CASCADE, related_name='subjectcategory')

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.TextField(default="Savol")
    subject_name = models.ForeignKey(Subject, to_field="name", default="Matematika", on_delete=models.CASCADE, related_name='question')
    subject_category = models.ForeignKey(SubjectCategory, to_field="name",
                                         on_delete=models.CASCADE, related_name='question', null=True, blank=True)
    difficulty_level = models.IntegerField(default=1, validators=[validate_difficulty_question])

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class WrongAnswer(models.Model):
    from users.models import User
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='wronganswers')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wronganswers')

    def __str__(self):
        return self.user_id
