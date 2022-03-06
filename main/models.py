from django.db import models
from filebrowser.fields import FileBrowseField


class Сarousel(models.Model):
	url = models.CharField('URL', max_length=100, db_index=True, help_text='Ссылка, например: /about/history/', default='')
	title = models.TextField(max_length=60, unique=True, verbose_name='Информация (всего 50 символов)')
	order = models.PositiveSmallIntegerField(db_index=True, default=1, unique=True, verbose_name='Позиция', help_text='Выберете позицию для сортировки')

	image = FileBrowseField(
		"Обложка",
		max_length=200,
		directory="carousel_cover/",
		extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp', '.webp'],
		format='image',
		blank=False,
	)

	class Meta:
		verbose_name_plural = 'Настройка карусели'
		verbose_name = 'Карусель'
		ordering = ['order']

	def __str__(self):
		return self.title
