# Generated by Django 4.0.3 on 2022-04-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Financial_literacy', '0002_alter_information_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='issued',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]