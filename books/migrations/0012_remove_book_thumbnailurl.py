# Generated by Django 3.2.4 on 2021-07-03 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='thumbnailUrl',
        ),
    ]
