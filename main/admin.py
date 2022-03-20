from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Сarousel


class СarouselAdmin(admin.ModelAdmin):
	list_display = ('title', 'order')
	list_display_links = ('title',)

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


admin.site.register(Сarousel, СarouselAdmin)
