# Generated by Django 3.2.12 on 2022-03-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='redirect_url',
            field=models.CharField(blank=True, help_text='Например: http://vt.fvp.su/Ryzhevo/Ryzhevo.html', max_length=50, verbose_name='Введите адрес стороннего сайта(если нужно)'),
        ),
    ]