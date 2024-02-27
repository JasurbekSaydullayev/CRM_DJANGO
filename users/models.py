from time import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .validators import check_phone_number

USER_TYPES = [
    ("O'qituvchi", "O'qituvchi"),
    ("O'quvchi", "O'quvchi")
]


class Group(models.Model):
    number_of_group = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number_of_group)


class User(AbstractUser):
    usertype = models.CharField(choices=USER_TYPES, default="O'quvchi")
    phone_number = models.CharField(validators=[check_phone_number])
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="users", null=True, blank=True)

    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Attendance(models.Model):
    attended = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.ForeignKey('quizapp.Subject', to_field="name", on_delete=models.CASCADE,
                                     related_name="attendances")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.subject_name)


class Result(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
    subject_name = models.ForeignKey('quizapp.Subject', to_field="name", on_delete=models.CASCADE,
                                     related_name="results")
    score = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.subject_name)
