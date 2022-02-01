# Generated by Django 3.2.8 on 2022-01-23 17:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(help_text='Ссылка, например: about', null=True, unique=True, verbose_name='URL-aдрес(Cлаг)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Краткое описание'),
        ),
    ]
