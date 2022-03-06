# Generated by Django 3.2.12 on 2022-03-06 07:46

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_alter_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Обложка статьи'),
        ),
    ]
