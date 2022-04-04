from django.db import models
from filebrowser.fields import FileBrowseField
from django.core.exceptions import ValidationError
from django.conf import settings


class СarouselMaster(models.Model):
	class Meta:
		verbose_name_plural = 'Настройка карусели'
		verbose_name = 'Карусель'

	def __str__(self):
		return 'Карусель'

	def clean(self):
		object_len = СarouselMaster.objects.count()
		if object_len == 1:
			object = СarouselMaster.objects.last()
			if self.pk != object.pk:
				raise ValidationError("Карусель уже существует! Отредактируйте старую или удалите и создайте новую.")


class Сarousel(models.Model):
	master = models.ForeignKey(
		СarouselMaster,
		default='',
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		verbose_name='Автор'
	)
	url = models.CharField(
		'URL',
		max_length=100,
		help_text='Ссылка, например: /about/history/',
		blank=True,
		default='')
	title = models.TextField(
		max_length=60,
		unique=True,
		verbose_name='Информация (50 символов)')

	image = FileBrowseField(
		"Обложка",
		max_length=200,
		directory=settings.FILEBROWSER_DIRECTORY_CAROUSEL,
		extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp', '.webp'],
		format='image',
		blank=False,
	)

	position = models.PositiveSmallIntegerField("Позиция", null=True)
	button = models.BooleanField("Показать кнопку 'Подробнее'", default=True)

	class Meta:
		verbose_name_plural = 'Настройка карусели'
		verbose_name = 'Карусель'
		ordering = ['position']

	def clean(self):
		if self.button and not self.url:
			raise ValidationError("Введите ссылку или отключите показ кнопки")

	def __str__(self):
		return self.title
