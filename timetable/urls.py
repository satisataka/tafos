from django.urls import path

from .views import TimetableWeekArchiveView

app_name = "timetable"


urlpatterns = [
	path('', TimetableWeekArchiveView.as_view(), name='timetable_now'),
	path('<int:year>/week/<int:week>', TimetableWeekArchiveView.as_view(), name='timetable'),
]
