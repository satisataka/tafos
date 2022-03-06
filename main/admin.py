from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Сarousel


class TinyMCEFlatPageAdmin(FlatPageAdmin):
	# form = TinyMCEFlatPageAdminForm
	fieldsets = (
		(None, {'fields': ('url', 'title', 'content', 'sites')}),
	)
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE(
			attrs={'cols': 80, 'rows': 30},
			mce_attrs={'style_formats': [
				{'title': 'Текст', 'format': 'p'},
				{'title': 'Заголовок', 'format': 'h1'},
				{'title': 'Подзаголовок 1', 'format': 'h2'},
				{'title': 'Подзаголовок 2', 'format': 'h3'},
				{'title': 'Цитата', 'format': 'blockquote'},
			]}
		)},
	}


class СarouselAdmin(admin.ModelAdmin):
	list_display = ('title', 'order')
	list_display_links = ('title',)
	list_editable = ('order',)

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
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)

