from django.shortcuts import render
from io import TextIOWrapper
from django import template
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Article, Author, Rubric


class ArticlesListView(ListView):
	model = Article
	context_object_name = 'all_articles'
	paginate_by = 10

	def get_queryset(self):
		qs = self.model.objects.all()
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
