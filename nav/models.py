from django.db import models
from filebrowser.fields import FileBrowseField
from django.conf import settings

class Menu(models.Model):
	name = models.CharField(db_index=True, unique=True, max_length=50, verbose_name='Название', help_text='Название должно быль уникальным')
	slug = models.SlugField(db_index=True, unique=True, verbose_name='URL-aдрес(Cлаг)', help_text='Ссылка, например: about')
	description = models.TextField(blank=True, verbose_name='Описание', help_text='Не обязательное поле')
	order = models.PositiveSmallIntegerField(db_index=True, default=1, verbose_name='Позиция', help_text='Выберете позицию для сортировки')
	hide = models.BooleanField(verbose_name='Скрыть', default=False)

	class Meta:
		verbose_name = 'Настройка Меню'
		verbose_name_plural = 'Меню'
		ordering = ['order', 'name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f'/{self.slug}/'


class MenuItem(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, verbose_name='Заголовок')
	description = models.TextField(max_length=500, blank=True, verbose_name='Описание', help_text='Не обязательное поле')
	slug = models.SlugField(db_index=True, unique=True, verbose_name='Cлаг', help_text='Ссылка, например: about')
	order = models.PositiveSmallIntegerField(db_index=True, default=1, verbose_name='Позиция', help_text='Выберете позицию для сортировки')
	hide = models.BooleanField(verbose_name='Скрыть', default=False)
	image = FileBrowseField(
		"Изображение",
		max_length=200,
		directory=settings.FILEBROWSER_DIRECTORY_NAVBAR_COVER,
		extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp', '.webp'],
		format='image',
		blank=True
	)

	class Meta:
		verbose_name = 'Пункт меню'
		verbose_name_plural = 'Пункты меню'
		ordering = ['order', 'title']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f'/{self.menu.slug}/{self.slug}/'
