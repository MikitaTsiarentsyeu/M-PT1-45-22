# Generated by Django 4.0.3 on 2022-04-10 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_question_author_question_author_a_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='issued',
        ),
    ]
