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
from django.conf.urls import handler400, handler403, handler404, handler500

from django.views.generic.base import RedirectView

handler404 = 'main.views.custom_page_not_found_view'
handler500 = 'main.views.custom_error_view'
handler403 = 'main.views.custom_permission_denied_view'
handler400 = 'main.views.custom_bad_request_view'

urlpatterns = [

	path('admin/filebrowser/', site.urls),
	path('grappelli/', include('grappelli.urls')),
	path('tinymce/', include('tinymce.urls')),
	path('admin/', admin.site.urls),
	path('', include('main.urls')),
]

''' + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) '''

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
