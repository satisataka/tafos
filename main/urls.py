from django.urls import path, include
from .views import MenuItemView, СarouselView
from django.views.generic import TemplateView


urlpatterns = [
	path('', СarouselView.as_view(), name='index'),
	path('donate/', TemplateView.as_view(template_name='main/donate.html'), name='donate'),
	path('worship/timetable/', include('timetable.urls')),
	path('novosti-obiteli/', include('articles.urls')),
	path('<slug:menu>/', MenuItemView.as_view(), name='menu_list'),
]
