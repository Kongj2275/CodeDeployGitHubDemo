# Generated by Django 3.0.5 on 2022-09-19 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_remove_question_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=600)),
                ('questionoption', models.CharField(max_length=600)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Course')),
            ],
        ),
    ]