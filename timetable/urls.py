from django.urls import path
from datetime import date

from .views import TimetableWeekArchiveView

app_name = "timetable"

urlpatterns = [
	path('', TimetableWeekArchiveView.as_view(
		year=int(date.today().year),
		week=int(date.today().isocalendar()[1])),
		name='timetable_now'),
	path('<int:year>/week/<int:week>', TimetableWeekArchiveView.as_view(), name='timetable'),
]
