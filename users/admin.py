from django.contrib import admin

from .models import User, Attendance, Group, Result


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_of_group']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'get_full_name', 'is_confirmed']
    search_fields = ['username']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'subject_name', 'date']


@admin.register(Result)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'subject_name', 'date', 'score']
