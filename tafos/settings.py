import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
# Take environment variables from .env file
env.read_env(BASE_DIR / '.env')

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

INSTALLED_APPS = [
	'django.contrib.contenttypes',
	'grappelli.dashboard',
	'grappelli',
	'filebrowser',
	'django.contrib.flatpages',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.sites',
	'django.contrib.sitemaps',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'main.apps.MainConfig',
	'timetable.apps.TimetableConfig',
	'nav.apps.NavConfig',
	'articles.apps.ArticlesConfig',
	'flatpage_tafos.apps.FlatpageTafosConfig',
	'tinymce',
	'robots'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': 'unix:/tmp/memcached.sock',
	}
}

SITE_ID = env.int('SITE_ID', 1)

ROOT_URLCONF = 'tafos.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'tafos.wsgi.application'

# Database
DATABASES = {
	'default': env.db()
}
ADMINS = [x.split(':') for x in env.list('DJANGO_ADMINS')]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'Europe/Moscow'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

FILEBROWSER_DIRECTORY = 'uploads/'
DIRECTORY = ''

ARTICLE_PAGINATE_BY = 10

X_FRAME_OPTIONS = 'SAMEORIGIN'

TINYMCE_DEFAULT_CONFIG = {
	'menubar': False,
	'branding': False,
	'theme': 'silver',
	'placeholder': 'Начните статью...',
	'height': 800,
	'width': 1300,
	'min_height': 500,
	'browser_spellcheck': True,  # Проверка орфографии
	'contextmenu': 'link image',
	'content_css': [
		'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css',
		os.path.join(STATIC_URL, 'tinymce/style.css')
	],
	'plugins':
		'''
		link image media visualblocks autolink fullscreen imagetools preview print quickbars wordcount nonbreaking lists paste

		''',
	'toolbar':
		'''
		fullscreen print preview | undo redo | styleselect | bold italic underline strikethrough removeformat |
		alignleft aligncenter alignright alignjustify | outdent indent | bullist numlist
		| link image media | visualblocks
		''',
	'formats': {
		'alignleft': {'selector': 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li', 'classes': 'text-start'},
		'aligncenter': {'selector': 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li', 'classes': 'text-center'},
		'alignright': {'selector': 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li', 'classes': 'text-end'},
		'alignjustify': {'selector': 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li', 'classes': 'text-justify'},
		'bold': {'inline': 'span', 'classes': 'fw-bold'},
		'italic': {'inline': 'span', 'classes': 'fst-italic'},
		'underline': {'inline': 'span', 'classes': 'text-decoration-underline'},
		'strikethrough': {'inline': 'span', 'classes': 'text-decoration-line-through'},
	},
	'style_formats': [
		{'title': 'Текст', 'format': 'p'},
		{'title': 'Подзаголовок 2', 'format': 'h2'},
		{'title': 'Подзаголовок 3', 'format': 'h3'},
		{'title': 'Цитата', 'format': 'blockquote'},
	],
	'nonbreaking_force_tab': True,
	'quickbars_insert_toolbar': 'image media',
	'quickbars_selection_toolbar': 'bold italic | aligncenter alignjustify | bullist | quicklink blockquote',
	# image setting
	'image_caption': True,
	'quickbars_image_toolbar': False,
	# media setting
	'media_poster': False,
	'media_alt_source': False,
	'media_dimensions': False,

	'paste_block_drop': True,
	'paste_as_text': True,

	'indentation': '20pt',
	'indent_use_margin': True,
}

TINYMCE_FILEBROWSER = True

# setting FileBrowser
# FILEBROWSER_NORMALIZE_FILENAME = True
FILEBROWSER_CONVERT_FILENAME = True
FILEBROWSER_VERSIONS = {
	'admin_thumbnail': {'verbose_name': 'Миниатюра (60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
	'thumbnail': {'verbose_name': 'Миниатюра (60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
	'cover': {'verbose_name': 'Для обложки (400px)', 'width': 500, 'height': '', 'opts': ''},
	'article': {'verbose_name': 'Для статьи (750px)', 'width': 750, 'height': '', 'opts': ''},
	'carousel': {'verbose_name': 'Для карусели (1920px)', 'width': 1920, 'height': '', 'opts': ''},
	'open_graph': {'verbose_name': 'open_graph(1200x630px)', 'width': 1200, 'height': 630, 'opts': 'crop'},
	'open_graph_vk': {'verbose_name': 'open_graph_vk(1200x536px)', 'width': 1200, 'height': 536, 'opts': 'crop'},
}
FILEBROWSER_ADMIN_VERSIONS = ['article']
FILEBROWSER_EXTENSIONS = {
	'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp', '.webp'],
	'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv'],
	'Video': [],
	'Audio': []
}

GRAPPELLI_INDEX_DASHBOARD = 'tafos.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = 'Введенский храм'
GRAPPELLI_CLEAN_INPUT_TYPES = False
GRAPPELLI_SWITCH_USER = True

# secure settings
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', False)
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', 0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', False)
SECURE_HSTS_RELOAD = env.bool('SECURE_HSTS_RELOAD', False)
SECURE_BROWSER_XSS_FILTER = env.bool('SECURE_BROWSER_XSS_FILTER', False)
SECURE_REFERRER_POLICY = env.str('SECURE_REFERRER_POLICY', None)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', False)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', False)
