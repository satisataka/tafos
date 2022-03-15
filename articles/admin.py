from django.contrib import admin
from .models import Article, Author, Rubric
from django import forms
from django.urls import reverse
from django.utils.html import format_html


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
		(None, {
			'classes': ('grp-collapse grp-open',),
			'fields': ('image',),
		}),
		(None, {

			'fields': ('content', 'status',),
		}),

		('Дата', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('creation_date', 'edit_date', 'published', 'user',),
		}),
	)
	list_display = ('title', 'description', 'author', 'rubric', 'status', 'published', 'edit_date', 'user_link',)
	list_display_links = ('title', 'description', 'user_link',)
	list_filter = ('title', 'rubric', 'author', 'user')
	list_editable = ('status',)
	search_fields = ('title', 'description')
	readonly_fields = ('published', 'creation_date', 'edit_date', 'user')
	prepopulated_fields = {'slug': ('title',)}

	def save_model(self, request, obj, form, change):
		if not obj.user:
			obj.user = request.user
		super().save_model(request, obj, form, change)

	def user_link(self, obj):
		url = reverse('admin:auth_user_change', args=(obj.user_id,))
		if obj.user.last_name or obj.user.first_name:
			return format_html("<a href='{}'>{} {}</a>", url, obj.user.first_name, obj.user.last_name,)
		else:
			return format_html("<a href='{}'>{}</a>", url, obj.user)

	user_link.short_description = "Пользователь"


class RubricAdmin(admin.ModelAdmin):
	list_display = ('name', 'order')
	list_display_links = ('name',)
	list_editable = ('order',)
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Rubric, RubricAdmin)
