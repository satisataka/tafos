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
