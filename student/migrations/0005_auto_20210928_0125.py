# Generated by Django 3.2.7 on 2021-09-27 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='userName',
        ),
    ]
