# Generated by Django 3.2.7 on 2021-09-27 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(editable=False, max_length=30, null=True),
        ),
    ]