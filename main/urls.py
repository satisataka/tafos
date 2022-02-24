from django.urls import path, include
from .views import MenuItemView
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
	path('', TemplateView.as_view(template_name='main/index.html'), name='index'),
	path('donate/', TemplateView.as_view(template_name='main/donate.html'), name='donate'),
	path('worship/timetable/', include('timetable.urls')),
	path('contacts/virtual/', RedirectView.as_view(url='http://vt.fvp.su/Ryzhevo/Ryzhevo.html'), name='virtual'),
	path('novosti-obiteli/', include('articles.urls')),
	path('<slug:menu>/', MenuItemView.as_view(), name='menu_list'),
]

