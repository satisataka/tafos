from django.urls import path
from .views import MenuItemView, –°arouselView

app_name = "main"

urlpatterns = [
	path('', –°arouselView.as_view(), name='index'),
	path('<slug:menu>/', MenuItemView.as_view(), name='menu_list'),
]
