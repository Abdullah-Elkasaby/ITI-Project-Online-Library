# Generated by Django 3.2.7 on 2021-09-24 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='onSale',
            field=models.BooleanField(default=False),
        ),
    ]