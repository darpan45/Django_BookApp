# Generated by Django 3.2.4 on 2021-06-27 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210627_1118'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
    ]