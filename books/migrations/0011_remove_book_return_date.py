# Generated by Django 3.2.7 on 2021-09-28 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='return_date',
        ),
    ]
