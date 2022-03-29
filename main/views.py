from django.views.generic import ListView
from nav.models import MenuItem, Menu
from django.views.generic.base import TemplateView
from .models import Сarousel
from timetable.models import TimeTableItem
from articles.models import Article
from datetime import datetime, timedelta
from django.shortcuts import render


class MenuItemView(ListView):
	model = MenuItem
	context_object_name = 'menu_items'

	def get_queryset(self):
		qs = self.model.objects.all()
		if self.kwargs.get('menu'):
			qs = qs.filter(hide=False, menu__slug=self.kwargs['menu'])
		return qs

	def get_context_data(self, **kwargs):
		context = super(MenuItemView, self).get_context_data(**kwargs)
		if self.kwargs.get('menu'):
			active_menu = Menu.objects.get(slug=self.kwargs['menu'])
			context['active_menu'] = {'name': active_menu.name, 'description': active_menu.description}
		return context


class СarouselView(TemplateView):

	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['carousel'] = Сarousel.objects.all()
		context['day_now'] = datetime.now().date()
		context['day_tomorrow'] = context['day_now'] + timedelta(days=1)
		try:
			context['timetable_now'] = TimeTableItem.objects.filter(date__day=context['day_now'])
		except TimeTableItem.DoesNotExist:
			context['timetable_now'] = None
		try:
			context['timetable_tomorrow'] = TimeTableItem.objects.filter(date__day=context['day_tomorrow'])
		except TimeTableItem.DoesNotExist:
			context['timetable_tomorrow'] = None

		context['news'] = Article.objects.filter(status='p')[:3]
		return context


def custom_page_not_found_view(request, exception):
	return render(request, "errors/404.html", status=404)


def custom_error_view(request, exception=None):
	return render(request, "errors/500.html", status=500)


def custom_permission_denied_view(request, exception=None):
	return render(request, "errors/403.html", status=403)


def custom_bad_request_view(request, exception=None):
	return render(request, "errors/400.html", status=400)
