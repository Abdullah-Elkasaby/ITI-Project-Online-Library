# Generated by Django 3.2.7 on 2021-09-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.DateField(null=True),
        ),
    ]
