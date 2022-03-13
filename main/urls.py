from django.urls import path
from .views import MenuItemView, СarouselView

app_name = "main"

urlpatterns = [
	path('', СarouselView.as_view(), name='index'),
	path('<slug:menu>/', MenuItemView.as_view(), name='menu_list'),
]
