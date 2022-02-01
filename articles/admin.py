from django.contrib import admin
from .models import Article, Author, Rubric
from django.db import models
from django.forms.widgets import Textarea, TextInput


class ArticleAdmin(admin.ModelAdmin):
	fields = [('title', 'slug'), 'author', 'description', 'content', 'rubric', 'published']
	list_display = ('title', 'author', 'description', 'rubric', 'published')
	list_display_links = ('title', 'author', 'description')
	list_filter = ('title', 'rubric', 'author')
	list_editable = ('rubric',)
	search_fields = ('author', 'title', 'description')
	readonly_fields = ('published',)
	prepopulated_fields = {'slug': ('title',)}
	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 70})},
		models.CharField: {'widget': TextInput(attrs={'size': 75})},
	}


class RubricAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Rubric, RubricAdmin)
