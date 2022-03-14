from django.conf import settings
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.sitemaps import Sitemap
from articles.models import Article, Rubric
from nav.models import Menu
from timetable.models import TimeTable
from django.contrib.flatpages.models import FlatPage


class ArticleSitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.9
	protocol = 'https'

	def items(self):
		return Article.objects.filter(status='p')

	def lastmod(self, obj):
		return obj.published


class ArticleListSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.8
	protocol = 'https'

	def items(self):
		articles = Article.objects.filter(status='p')
		paginator = Paginator(articles, settings.ARTICLE_PAGINATE_BY)
		return paginator.page_range

	def location(self, page):
		return reverse('articles:all_articles') + f'?page={page}'

	def lastmod(self, page):
		art = Article.objects.filter(status='p').order_by('-published').last()
		if art:
			return art.published


class ArticleListRubricSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.8
	protocol = 'https'

	def items(self):
		list_rubric_article = []
		for rubric in Rubric.objects.all():
			articles = Article.objects.filter(status='p', rubric=rubric)
			paginator = Paginator(articles, settings.ARTICLE_PAGINATE_BY)
			for p in paginator.page_range:
				list_rubric_article.append((rubric.slug, p))
		return list_rubric_article

	def location(self, page):
		return reverse('articles:rubric_articles', kwargs={'slug': page[0]}) + f'?page={page[1]}'

	def lastmod(self, page):
		rub = Rubric.objects.get(slug=page[0])
		art = Article.objects.filter(status='p', rubric=rub).order_by('-published').last()
		if art:
			return art.published


class RubricSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.8
	protocol = 'https'

	def items(self):
		return Rubric.objects.all()

	def lastmod(self, rub):
		art = Article.objects.filter(status='p', rubric=rub).order_by('-published').last()
		if art:
			return art.published


class MenuSitemap(Sitemap):
	priority = 0.7
	protocol = 'https'

	def items(self):
		return Menu.objects.all().filter(hide=False)

	def lastmod(self, menu):
		if menu.slug == 'novosti-obiteli':
			art = Article.objects.filter(status='p').order_by('-published').last()
			if art:
				return art.published

	def changefreq(self, menu):
		if menu.slug == 'novosti-obiteli':
			return 'daily'
		else:
			return 'monthly'


class FlatPageSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.7
	protocol = 'https'

	def items(self):
		return FlatPage.objects.all()


class TimeTableSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.8
	protocol = 'https'

	def items(self):
		timetable_absolute_url = [reverse('timetable:timetable_now')]
		for obj in TimeTable.objects.all():
			if obj.get_absolute_url() in timetable_absolute_url:
				continue
			else:
				timetable_absolute_url.append(obj.get_absolute_url())
		return timetable_absolute_url

	def location(self, item):
		return item


class StaticSitemap(Sitemap):
	changefreq = "yearly"
	priority = 0.8
	protocol = 'https'

	def items(self):
		return ['donate', 'virtual']

	def location(self, item):
		return reverse(item)


class MainPageSitemap(Sitemap):
	changefreq = "daily"
	priority = 1
	protocol = 'https'

	def items(self):
		return ['main:index']

	def location(self, item):
		return reverse(item)

	def lastmod(self, page):
		art = Article.objects.filter(status='p').order_by('-published').last()
		return art.published
