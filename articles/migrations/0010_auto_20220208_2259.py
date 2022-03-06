# Generated by Django 3.2.8 on 2022-02-08 19:59

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content_2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='content_3',
        ),
        migrations.RemoveField(
            model_name='article',
            name='cover',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default='', verbose_name='Содержание'),
        ),
    ]
