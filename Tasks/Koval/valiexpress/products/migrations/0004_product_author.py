# Generated by Django 4.0.3 on 2022-04-05 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_authors_author_rename_categories_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.author'),
        ),
    ]
