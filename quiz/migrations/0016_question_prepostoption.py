# Generated by Django 3.0.5 on 2022-09-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_shortquestion_prepostoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='prepostoption',
            field=models.CharField(default='Postrecord', max_length=200),
            preserve_default=False,
        ),
    ]
