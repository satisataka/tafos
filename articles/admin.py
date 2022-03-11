from django.contrib import admin
from .models import Article, Author, Rubric
from django import forms


class ArticleModelForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ArticleModelForm, self).__init__(*args, **kwargs)
		self.fields['author'].empty_label = '-- Нет автора --'
		self.fields['title'].widget.attrs['style'] = 'width:800px; height:40px;'
		self.fields['description'].widget.attrs['style'] = "width: 800px; height: 200px;"


class ArticleAdmin(admin.ModelAdmin):
	form = ArticleModelForm
	fieldsets = (
		('Зоголовок', {
			'classes': ('grp-collapse grp-open',),
			'fields': ('title', 'slug', 'author', 'rubric', 'description',),
		}),
		('Обложка статьи', {
			'classes': ('grp-collapse grp-open',),
			'fields': ('image',),
		}),
		('Основное', {

			'fields': ('content',),
		}),
		('Дата', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('published',),
		}),
	)

	list_display = ('title', 'author', 'description', 'rubric', 'published')
	list_display_links = ('title', 'author', 'description')
	list_filter = ('title', 'rubric', 'author')
	list_editable = ('rubric',)
	search_fields = ('author', 'title', 'description')
	readonly_fields = ('published',)
	prepopulated_fields = {'slug': ('title',)}


class RubricAdmin(admin.ModelAdmin):
	list_display = ('name', 'order')
	list_display_links = ('name',)
	list_editable = ('order',)
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Rubric, RubricAdmin)
