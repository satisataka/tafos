from django.db import models
from django.contrib.flatpages.models import FlatPage
from filebrowser.fields import FileBrowseField
from django.conf import settings


class NewFlatpage(models.Model):
	flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
	image = FileBrowseField(
		"Обложка",
		max_length=200,
		directory=settings.FILEBROWSER_DIRECTORY_FLATPAGES_COVER,
		extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp', '.webp'],
		format='image',
		blank=True
	)

	def __str__(self):
		return self.flatpage.title

	class Meta:
		verbose_name = "Содержание страницы"
		verbose_name_plural = "Содержание страницы"
