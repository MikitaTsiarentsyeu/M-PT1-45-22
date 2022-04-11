# Generated by Django 4.0.3 on 2022-04-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upload')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]