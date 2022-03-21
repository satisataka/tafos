from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Сarousel, СarouselMaster
from grappelli.forms import GrappelliSortableHiddenMixin
from django.urls import reverse
from django.utils.html import format_html
import os
from tafos.settings import MEDIA_URL


class СarouselInline(GrappelliSortableHiddenMixin, admin.TabularInline):
	fields = ('url', 'button', 'title', 'image', "position",)
	model = Сarousel
	verbose_name = "Слайд"
	max_num = 10
	extra = 0

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE(
			attrs={'cols': 80, 'rows': 30},
			mce_attrs={
				'style_formats': [{'title': 'Текст', 'format': 'p'}],
				'placeholder': '',
				'min_height': 80,
				'height': 150,
				'width': 500,
				'toolbar': "",
				'plugins':
					'''
					wordcount nonbreaking paste
					''',
			}
		)},
	}


class СarouselAdmin(admin.ModelAdmin):
	inlines = [СarouselInline]

	class Meta:
		verbose_name_plural = 'Статьи'
		verbose_name = 'Статья'

	list_display = ('edit_link', 'carusel_link', 'slide_image_link',)
	list_display_links = ('edit_link', 'carusel_link', 'slide_image_link')

	def carusel_link(self, obj):
		count = obj.сarousel_set.count()
		url = reverse('admin:main_сarouselmaster_change', args=(obj.id,))
		if count % 10 == 0 or 11 <= count % 100 <= 14 or 5 <= count % 10 <= 9:
			return format_html('<a href="{}">{} слайдов</a>', url, count)
		elif 2 <= count % 10 <= 4:
			return format_html('<a href="{}">{} слайда', url, count)
		else:
			return format_html('<a href="{}">{} слайд</a>', url, count)

	carusel_link.short_description = "Всего:"

	def slide_image_link(self, obj):
		objects = obj.сarousel_set.all()
		url = reverse('admin:main_сarouselmaster_change', args=(obj.id,))
		return format_html(' '.join('<a href="{}"><img src="{}"/></a>'.format(obj.image.url, os.path.join(MEDIA_URL, obj.image.version_path("admin_thumbnail"))) for obj in objects))

	slide_image_link.short_description = "Слайды:"

	def edit_link(self, obj):
		url = reverse('admin:main_сarouselmaster_change', args=(obj.id,))
		return format_html('<a href="{}">{}</a>', url, 'Редактировать слайды')

	edit_link.short_description = ""


admin.site.register(СarouselMaster, СarouselAdmin)
