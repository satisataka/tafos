# Generated by Django 3.2.8 on 2022-01-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220123_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubric',
            name='slug',
            field=models.SlugField(help_text='Ссылка, например: about', null=True, unique=True, verbose_name='URL-aдрес(Cлаг)'),
        ),
    ]
