# Generated by Django 3.2.7 on 2021-09-27 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
