# Generated by Django 5.0.1 on 2024-01-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_created_at_article_priority_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesubcategory',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='author name'),
        ),
    ]
