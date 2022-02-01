from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):
	name = models.CharField(max_length=50, unique=True, verbose_name='Фамилия и имя', help_text='Пример: Игумен Феофан (Кузнецов)')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Авторы'
		verbose_name = 'Автор'
		ordering = ['name']


class Rubric(models.Model):
	name = models.CharField(max_length=20, db_index=True, verbose_name='Название рубрики', help_text='Пример: Новости Обители')
	slug = models.SlugField(db_index=True, unique=True, verbose_name='URL-aдрес(Cлаг)', help_text='Ссылка, например: about')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Рубрики'
		verbose_name = 'Рубрика'
		ordering = ['name']


"validators=[validators.RegexValidator(regex='^.{4,}$')],"


class Article(models.Model):
	author = models.ForeignKey(Author, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Выберете автора')
	description = models.TextField(max_length=200, null=False, blank=False, verbose_name='Краткое описание')
	title = models.CharField(max_length=50, unique=True, verbose_name='Название')
	content = RichTextUploadingField(null=False, blank=False, verbose_name='Содержание')
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
	rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрики')
	slug = models.SlugField(db_index=True, unique=True, verbose_name='URL-aдрес(Cлаг)', help_text='Ссылка, например: about')
	'''class Kinds(models.TextChoices):
		BUY = 'b', 'Куплю'
		SELL = 's', 'Продам'
		EXCHANGE = 'c', 'Обменяю'
		RENT = 'r', 'Сдам'
		__empty__ = '-- Выберете тип публикуемого объявления --'

	kind = models.CharField(max_length=1, choices=Kinds.choices, null=True, verbose_name='Тип объявления')'''

	class Meta:
		verbose_name_plural = 'Статьи'
		verbose_name = 'Статья'
		ordering = ['-published']

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
