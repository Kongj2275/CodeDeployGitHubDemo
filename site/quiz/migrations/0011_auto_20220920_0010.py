# Generated by Django 3.0.5 on 2022-09-19 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20220919_2316'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShortAnswer',
            new_name='ShortQuestion',
        ),
    ]
