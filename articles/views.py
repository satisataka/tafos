from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Article, Rubric
from django.conf import settings


class ArticlesListView(ListView):
	model = Article
	context_object_name = 'all_articles'
	paginate_by = settings.ARTICLE_PAGINATE_BY

	def get_queryset(self):
		qs = self.model.objects.filter(status='p')
		if self.kwargs.get('slug'):
			qs = qs.filter(rubric__slug=self.kwargs['slug'])
		return qs

	def get_context_data(self, **kwargs):
		context = super(ArticlesListView, self).get_context_data(**kwargs)
		context['rubric'] = Rubric.objects.all()
		if self.kwargs.get('slug'):
			active_rubric = Rubric.objects.get(slug=self.kwargs['slug'])
			context['active_rubric'] = {'name': active_rubric.name, 'slug': active_rubric.slug}
		return context


class ArticleDetailView(DetailView):
	model = Article
	context_object_name = 'article'

	def get_queryset(self):
		qs = self.model.objects.filter(status='p', slug=self.kwargs.get('slug'))
		return qs
