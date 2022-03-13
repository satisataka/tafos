from django.contrib.sitemaps import Sitemap
from articles.models import Article
from nav.models import Menu, MenuItem

class ArticleSitemap(Sitemap):

	changefreq = 'weekly'
	priority = 0.9
	protocol = 'https'

	def items(self):
		return Article.objects

	def lastmod(self, obj):
		return obj.published


class MenuSitemap(Sitemap):
	changefreq = "always"
	priority = 0.8
	protocol = 'https'

	def items(self):
		return Menu.objects.all().filter(hide=False)


class MenuItemSitemap(Sitemap):
	changefreq = "always"
	priority = 0.8
	protocol = 'https'

	def items(self):
		return MenuItem.objects.all().filter(hide=False)
