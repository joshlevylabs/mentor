# Generated by Django 3.1.4 on 2021-04-01 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20210401_0237'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Notes',
        ),
    ]
