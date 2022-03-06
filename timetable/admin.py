from django.contrib import admin
from .models import TimeTable, TimeTableItem, ListChurchService
from django import forms
from django.db import models
from django.forms.widgets import TimeInput, DateInput
from django.urls import reverse
from django.utils.html import format_html


class CustomBarModelForm(forms.ModelForm):
	class Meta:
		fields = '__all__'
		model = TimeTableItem

	def __init__(self, *args, **kwargs):
		super(CustomBarModelForm, self).__init__(*args, **kwargs)
		self.fields['service'].queryset = ListChurchService.objects.filter(hide=False)


class TimeTableItemInline(admin.StackedInline):
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)
	form = CustomBarModelForm
	model = TimeTableItem
	formfield_overrides = {
		# 'rows':20, 'cols':5
		models.TimeField: {'widget': TimeInput(
			format='%H:%M',
			attrs={
				'type': "time",
				'style':
				'''
				font-family: Arial,sans-serif;
				font-size: 12px;
				font-weight: bold;
				color: #555;
				border: 1px solid #ccc;
				-moz-border-radius:
				3px;-webkit-border-radius:
				3px;border-radius: 3px;
				padding: 5px 5px;
				box-shadow: inset 0 1px 3px 0 #eee;
				'''
			},
		)},
	}
	show_change_link = False
	verbose_name = 'Богослужение'
	verbose_name_plural = 'Богослужения'

	def get_extra(self, request, obj=None, **kwargs):
		extra = 1
		if obj:
			return 0
		return extra


class TimeTableAdmin(admin.ModelAdmin):
	list_display = ['day', 'day_of_week', 'view_service_link']
	list_filter = ['day']
	ordering = ['-day']
	inlines = [TimeTableItemInline]
	formfield_overrides = {
		# 'rows':20, 'cols':5
		models.DateField: {'widget': DateInput(attrs={
			'type': 'date',
			'style':
				'''
				font-family: Arial,sans-serif;
				font-size: 12px;
				font-weight: bold;
				color: #555;
				border: 1px solid #ccc;
				-moz-border-radius:
				3px;-webkit-border-radius:
				3px;border-radius: 3px;
				padding: 5px 5px;
				box-shadow: inset 0 1px 3px 0 #eee;
				'''
		})},
	}

	def view_service_link(self, obj):
		count = obj.timetableitem_set.count()
		url = reverse("admin:timetable_listchurchservice_changelist")
		if count % 10 == 0 or 11 <= count % 100 <= 14 or 5 <= count % 10 <= 9:
			return format_html('<a href="{}">{} cлужб</a>', url, count)
		elif 2 <= count % 10 <= 4:
			return format_html('<a href="{}">{} cлужбы</a>', url, count)
		else:
			return format_html('<a href="{}">{} cлужба</a>', url, count)

	view_service_link.short_description = "Богослужений"


class ListChurchServiceAdmin(admin.ModelAdmin):
	fields = [('name', 'hide')]
	list_display = ['name', 'hide']
	list_filter = ['hide']
	list_editable = ['hide']
	list_display_links = ['name']
	ordering = ['name']
	actions = None


admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(ListChurchService, ListChurchServiceAdmin)
