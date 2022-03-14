from django.urls import path
from .views import ArticlesListView, ArticleDetailView

app_name = "articles"

urlpatterns = [
	path('', ArticlesListView.as_view(), name='all_articles'),
	path('<slug:slug>/', ArticlesListView.as_view(), name='rubric_articles'),
	path('<rubric>/<slug:slug>/', ArticleDetailView.as_view(), name='detail_article'),
]
