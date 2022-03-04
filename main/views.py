from django.views.generic import ListView
from nav.models import MenuItem, Menu
from django.views.generic.base import TemplateView
from .models import Сarousel
from timetable.models import TimeTable, TimeTableItem
from articles.models import Article
from datetime import datetime, date, time, timedelta


class MenuItemView(ListView):
	model = MenuItem
	context_object_name = 'menu_items'

	def get_queryset(self):
		qs = self.model.objects.all()
		if self.kwargs.get('menu'):
			qs = qs.filter(menu__slug=self.kwargs['menu'])
		return qs

	def get_context_data(self, **kwargs):
		context = super(MenuItemView, self).get_context_data(**kwargs)
		if self.kwargs.get('menu'):
			active_menu = Menu.objects.get(slug=self.kwargs['menu'])
			context['active_menu'] = {'name': active_menu.name}
		return context


class СarouselView(TemplateView):

	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['carousel'] = Сarousel.objects.all()
		day_now = datetime.now().date()
		day_tomorrow = day_now + timedelta(days=1)

		context['day_now'] = day_now
		context['day_tomorrow'] = day_tomorrow
		try:
			context['timetable_now'] = TimeTableItem.objects.filter(date__day=day_now)
		except TimeTableItem.DoesNotExist:
			context['timetable_now'] = None
		try:
			context['timetable_tomorrow'] = TimeTableItem.objects.filter(date__day=day_tomorrow)
		except TimeTableItem.DoesNotExist:
			context['timetable_tomorrow'] = None

		context['news'] = Article.objects.all()[:3]
		print(context['news'])
		return context
