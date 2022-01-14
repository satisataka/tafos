from django.urls import path
from .views import static_page
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
	path('', TemplateView.as_view(template_name='main/index.html'), name='index'),

	path('contacts/virtual/', RedirectView.as_view(url='http://vt.fvp.su/Ryzhevo/Ryzhevo.html'), name='virtual'),
	path('<slug:menu>/<slug:sub_menu>/', static_page, name='static_page'),
	path('<slug:menu>/', static_page, name='static_page'),
]
