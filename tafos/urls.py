"""tafos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from django.contrib.flatpages import views
from django.views.generic import TemplateView
from django.contrib.sitemaps import views as sitemap_view
from django.views.generic.base import RedirectView
from .settings import DEBUG

import tafos.sitemaps as sitemaps

sitemaps = {
	'MainPage': sitemaps.MainPageSitemap,
	'Article': sitemaps.ArticleSitemap,
	'Rubric': sitemaps.RubricSitemap,
	'Menu': sitemaps.MenuSitemap,
	'TimeTable': sitemaps.TimeTableSitemap,
	'Static': sitemaps.StaticSitemap,
	'ArticleList': sitemaps.ArticleListSitemap,
	'ArticleListRubric': sitemaps.ArticleListRubricSitemap,
	'FlatPage': sitemaps.FlatPageSitemap,
}

handler404 = 'main.views.custom_page_not_found_view'
handler500 = 'main.views.custom_error_view'
handler403 = 'main.views.custom_permission_denied_view'
handler400 = 'main.views.custom_bad_request_view'

urlpatterns = [
	path('admin/filebrowser/', site.urls),
	path('grappelli/', include('grappelli.urls')),
	path('tinymce/', include('tinymce.urls')),
	path('admin1482839/', admin.site.urls),
	path('robots.txt', include('robots.urls')),
	path('sitemap.xml', sitemap_view.index, {'sitemaps': sitemaps}),
	path('sitemap-<section>.xml', sitemap_view.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('novosti-obiteli/', include('articles.urls', namespace='articles'), name='articles'),
	path('donate/', TemplateView.as_view(template_name='main/donate.html'), name='donate'),
	path('school/', views.flatpage, {'url': '/school/'}, name='school'),
	path('worship/timetable/', include('timetable.urls', namespace='timetable'), name='timetable'),
	path('contacts/virtual/', RedirectView.as_view(url='http://vt.fvp.su/Ryzhevo/Ryzhevo.html'), name='virtual'),
	path('', include('main.urls', namespace='main'), name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not DEBUG:
	urlpatterns += path('<path:url>', views.flatpage, name='django.contrib.flatpages.views.flatpage'),
