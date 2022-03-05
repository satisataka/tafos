from django.db import models
from filebrowser.fields import FileBrowseField


class Menu(models.Model):
	name = models.CharField(db_index=True, unique=True, max_length=50, verbose_name='Название', help_text='Название должно быль уникальным')
	slug = models.SlugField(db_index=True, unique=True, verbose_name='URL-aдрес(Cлаг)', help_text='Ссылка, например: about')
	description = models.TextField(blank=True, verbose_name='Описание', help_text='Не обязательное поле')
	order = models.PositiveSmallIntegerField(db_index=True, default=1, verbose_name='Позиция', help_text='Выберете позицию для сортировки')
	hide = models.BooleanField(verbose_name='Скрыть', default=False)

	class Meta:
		verbose_name = 'Меню'
		verbose_name_plural = 'Меню'
		ordering = ['order', 'name']
	"""
	def save(self, *args, **kwargs):
		'''
		Расставляем по позиции MenuItem, после сохранения
		'''
		super(Menu, self).save(*args, **kwargs)

		current = 1
		for item in MenuItem.objects.filter(menu=self).order_by('order'):
			item.order = current
			item.save()
			current += 1
	"""

	def __str__(self):
		return self.name


class MenuItem(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, verbose_name='Заголовок')
	description = models.TextField(max_length=500, blank=True, verbose_name='Описание', help_text='Не обязательное поле')
	slug = models.SlugField(db_index=True, unique=True, verbose_name='URL-aдрес(Cлаг)', help_text='Ссылка, например: about')
	order = models.PositiveSmallIntegerField(db_index=True, default=1, verbose_name='Позиция', help_text='Выберете позицию для сортировки')
	hide = models.BooleanField(verbose_name='Скрыть', default=False)
	image = FileBrowseField(
		"Изображение",
		max_length=200,
		directory="menu_images_cover/",
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
