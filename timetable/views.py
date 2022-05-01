from django.views.generic.dates import WeekArchiveView
from django.http import Http404
from django.utils.timezone import now
from .models import TimeTable


class TimetableWeekArchiveView(WeekArchiveView):
	queryset = TimeTable.objects.all()
	allow_future = True
	week_format = "%W"
	date_field = 'day'
	allow_empty = True

	def get_week(self):
		try:
			month = super().get_week()
		except Http404:
			month = now().strftime(self.get_week_format())
		return month

	def get_year(self):
		try:
			year = super().get_year()
		except Http404:
			year = now().strftime(self.get_year_format())

		return year

	def get_ordering(self):
		ordering = self.request.GET.get('-day')
		return ordering
