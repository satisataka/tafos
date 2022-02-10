from django.db import models
from tinymce.models import HTMLField

from filebrowser.fields import FileBrowseField



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


"validators=[validators.RegexValidator(regex='^.{4,}$')],"


class Article(models.Model):
	slug = models.SlugField(default='', db_index=True, unique=True, verbose_name='URL-aдрес(Cлаг)', help_text='Ссылка, например: about')
	title = models.CharField(max_length=50, unique=True, verbose_name='Название')
	author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Выберете автора')
	description = models.TextField(null=False, blank=False, verbose_name='Краткое описание')
	content = HTMLField(default='', null=False, blank=False, verbose_name='Содержание')
	rubric = models.ForeignKey('Rubric', default='', on_delete=models.PROTECT, verbose_name='Рубрики')
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
	image = FileBrowseField("Изображение", max_length=200, directory="images_cover/", extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'], format='image', blank=True)

	class Meta:
		verbose_name_plural = 'Статьи'
		verbose_name = 'Статья'
		ordering = ['-published']

	def __str__(self):
		return self.title


	"""def title_and_price(self):
		if self.price:
			return '{} ({:,.0f} руб.)'.format(self.title, self.price).replace(',', ' ')
		else:
			return self.title

	title_and_price.short_description = 'Название и цена'"""

	"""def clean(self):
		errors = {}
		if not self.content:
			errors['content'] = ValidationError('Укажите описание')
		if not self.price or self.price < 0:
			errors['price'] = ValidationError('Укажите правильную цену')

		if errors:
			raise ValidationError(errors)"""