from django.contrib import admin
from .models import Menu, MenuItem
from django import forms
from django.core.exceptions import ValidationError

from grappelli.forms import GrappelliSortableHiddenMixin


class CustomMenuItemForm(forms.BaseInlineFormSet):
	def clean(self):
		"""
		Проверяем уникальность полей title и url в наборе форм
		"""
		super().clean()
		for form in self.forms:
			if any(self.errors):
				return
			titles = []
			errors = []
			for form in self.forms:
				if self.can_delete and self._should_delete_form(form):
					continue
				title = form.cleaned_data.get('title')
				if title in titles:
					errors.append(ValidationError("Заголовoк {} повторяется. (Это поле должно быть уникальным)".format(title)))
				titles.append(title)
			raise ValidationError(errors)


class MenuItemInline(GrappelliSortableHiddenMixin, admin.StackedInline):
	model = MenuItem
	formset = CustomMenuItemForm

	fieldsets = (
		('', {
			'classes': ('grp-collapse grp-open',),
			'fields': ('title', 'slug', 'description', 'image'),
		}),

		('Прочее', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('hide', 'order', 'redirect_url'),
		}),
	)
	sortable_field_name = "order"

	inline_classes = ('grp-collapse grp-open',)

	def get_extra(self, request, obj=None, **kwargs):
		"""
		Если новый объект Menu, добавить один MenuItem.
		Если редактируется, то 0.
		"""
		extra = 1
		if obj:
			return 0
		return extra


class MenuAdmin(admin.ModelAdmin):
	inlines = [MenuItemInline]
	fields = [('name', 'slug'), 'order', 'description', 'hide']
	list_display = ['name', 'slug', 'view_itemmenu_link', 'order']
	list_display_links = ['name', 'slug']
	ordering = ['order', 'name']
	list_editable = ['order']
	prepopulated_fields = {'slug': ('name',)}

	def view_itemmenu_link(self, obj):
		count = obj.menuitem_set.count()
		return count
	view_itemmenu_link.short_description = "Подразделов"


admin.site.register(Menu, MenuAdmin)
