# Generated by Django 5.0.2 on 2024-02-27 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hashed_password',
        ),
    ]
