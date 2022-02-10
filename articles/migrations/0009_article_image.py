# Generated by Django 3.2.8 on 2022-02-08 16:45

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_article_content_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Image'),
        ),
    ]