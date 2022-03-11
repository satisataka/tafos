from django.views.generic.dates import WeekArchiveView
from .models import TimeTable


class TimetableWeekArchiveView(WeekArchiveView):
	queryset = TimeTable.objects.all()
	allow_future = True
	week_format = "%W"
	date_field = 'day'
	allow_empty = True

	def get_ordering(self):
		ordering = self.request.GET.get('-day')
		return ordering

	def get_context_data(self, **kwargs):
		context = super(TimetableWeekArchiveView, self).get_context_data(**kwargs)
		print(context)
		return context

	def render_to_response(self, context, **response_kwargs):
		c = super().render_to_response(context, **response_kwargs)
		url_timetable = [url for url in self.request.path.split('/') if url]
		index_url = url_timetable.index('timetable')
		if url_timetable[index_url + 1:]:
			self.url = True
		else:
			self.url = False

		print(self.url)
		print(self.__dict__)
		return c
