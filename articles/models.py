from django.db import models
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from datetime import datetime
from django.utils.timezone import get_current_timezone
from django.contrib.auth import get_user_model
from django.conf import settings


def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]


class Author(models.Model):
	name = models.CharField(max_length=70, unique=True, verbose_name='Фамилия и имя', help_text='Пример: Игумен Феофан (Кузнецов)')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Авторы'
		verbose_name = 'Автор'
		ordering = ['name']


class Rubric(models.Model):
	name = models.CharField(max_length=50, db_index=True, verbose_name='Название рубрики', help_text='Пример: Новости Обители')
	slug = models.SlugField(default='', db_index=True, unique=True, verbose_name='URL-aдрес(Cлаг)', help_text='Ссылка, например: about')
	order = models.PositiveSmallIntegerField(db_index=True, default=1, verbose_name='Позиция', help_text='Выберете позицию для сортировки')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Рубрики'
		verbose_name = 'Рубрика'
		ordering = ['order', 'name']

	def get_absolute_url(self):
		return f'/novosti-obiteli/{self.slug}/'


class Article(models.Model):
	STATUS_CHOICES = (
		('d', 'Черновик'),
		('p', 'Опубликовано'),
	)

	status = models.CharField(
		max_length=1,
		null=False,
		blank=False,
		choices=STATUS_CHOICES,
		default='d',
		verbose_name='Статус'
	)
	title = models.CharField(
		max_length=50,
		unique=True,
		verbose_name='Название статьи'
	)
	slug = models.SlugField(
		db_index=True,
		unique=True,
		default='',
		verbose_name='URL-aдрес(Cлаг)',
		help_text='Ссылка, например: about'
	)
	author = models.ForeignKey(
		Author,
		on_delete=models.PROTECT,
		null=True,
		blank=True,
		verbose_name='Автор'
	)
	description = models.TextField(
		max_length=500,
		null=False,
		blank=False,
		verbose_name='Краткое описание'
	)
	content = HTMLField(
		default='',
		null=False,
		blank=False,
		verbose_name='Содержание'
	)
	rubric = models.ForeignKey(
		Rubric,
		default='',
		on_delete=models.PROTECT,
		verbose_name='Рубрика'
	)
	creation_date = models.DateTimeField(
		auto_now_add=True,
		db_index=True,
		verbose_name='Дата создания'
	)
	edit_date = models.DateTimeField(
		db_index=True,
		null=True,
		verbose_name='Дата редактирования'
	)
	published = models.DateTimeField(
		db_index=True,
		null=True,
		verbose_name='Дата публикации'
	)
	image = FileBrowseField(
		"Обложка статьи",
		max_length=200,
		directory="articles_cover/",
		extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp', '.webp'],
		format='image',
		blank=True
	)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET(get_sentinel_user),
		default=None,
		null=True,
		verbose_name='Пользователь',
	)

	class Meta:
		verbose_name_plural = 'Все статьи'
		verbose_name = 'Статья'
		ordering = ['status', '-published', '-edit_date']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.old_status = self.status

	def save(self, *args, **kwargs):
		self.edit_date = datetime.now(tz=get_current_timezone())
		if self.status == 'p' and self.old_status == 'd':
			self.published = datetime.now(tz=get_current_timezone())
		if self.status == 'd':
			self.published = None
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f'/novosti-obiteli/{self.rubric.slug}/{self.slug}/'

	def _get_full_name(self):
		"Returns the person's full name."
		return '%s %s' % (self.user.first_name, self.user.last_name)

	user_full_name = property(_get_full_name)
