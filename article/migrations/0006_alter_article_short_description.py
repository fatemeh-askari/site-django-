# Generated by Django 5.0.1 on 2024-01-16 10:56

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_remove_articlesubcategory_author_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='short description'),
        ),
    ]
