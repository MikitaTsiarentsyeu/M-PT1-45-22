# Generated by Django 4.0.3 on 2022-04-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('title', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField(blank=True)),
                ('id', models.FloatField(blank=True, primary_key=True, serialize=False)),
                ('rightAnswer', models.FloatField(max_length=10)),
            ],
        ),
    ]
