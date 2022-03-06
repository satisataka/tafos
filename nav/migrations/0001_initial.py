# Generated by Django 3.2.12 on 2022-03-06 07:47

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Название должно быль уникальным', max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Ссылка, например: about', unique=True, verbose_name='URL-aдрес(Cлаг)')),
                ('description', models.TextField(blank=True, help_text='Не обязательное поле', verbose_name='Описание')),
                ('order', models.PositiveSmallIntegerField(db_index=True, default=1, help_text='Выберете позицию для сортировки', verbose_name='Позиция')),
                ('hide', models.BooleanField(default=False, verbose_name='Скрыть')),
            ],
            options={
                'verbose_name': 'Настройка Меню',
                'verbose_name_plural': 'Меню',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, help_text='Не обязательное поле', max_length=500, verbose_name='Описание')),
                ('slug', models.SlugField(help_text='Ссылка, например: about', unique=True, verbose_name='Cлаг')),
                ('order', models.PositiveSmallIntegerField(db_index=True, default=1, help_text='Выберете позицию для сортировки', verbose_name='Позиция')),
                ('hide', models.BooleanField(default=False, verbose_name='Скрыть')),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Изображение')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.menu')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'ordering': ['order', 'title'],
            },
        ),
    ]