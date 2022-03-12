from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from .models import NewFlatpage
from tinymce.widgets import TinyMCE
from django.db import models


class NewFlatpageInline(admin.StackedInline):
	inline_classes = ('grp-collapse grp-open',)
	model = NewFlatpage
	verbose_name = "Содержание"


class FlatPageNewAdmin(FlatPageAdmin):
	inlines = [NewFlatpageInline]
	list_display = ('url', 'title')
	list_filter = ('sites', 'title')
	search_fields = ('url', 'title')
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


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageNewAdmin)
