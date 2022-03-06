import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=l$hxz2gyo7&%_ix*^*6r661kjnjd03=5!vzynn-0$5nh!*2z_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
	ALLOWED_HOSTS = []
else:
	ALLOWED_HOSTS = ['194.58.122.168', 'satisataka.ru']


# Application definition

INSTALLED_APPS = [
	'django.contrib.contenttypes',
	'grappelli.dashboard',
	'grappelli',
	'filebrowser',
	'django.contrib.flatpages',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.sites',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'main.apps.MainConfig',
	'timetable.apps.TimetableConfig',
	'nav.apps.NavConfig',
	'articles.apps.ArticlesConfig',
	'tinymce',
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
]

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': 'unix:/tmp/memcached.sock',
	}
}

if DEBUG:
	SITE_ID = 2
else:
	SITE_ID = 1

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
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': BASE_DIR / 'db.tafos',
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'tafos_db',
			'USER': 'tafos',
			'PASSWORD': 'tafos_db_password_kozlov',
			'HOST': 'localhost',
			'PORT': '',
		}
	}

ADMINS = [('Artem Kozlov', 'kozlov0013@gmail.com'), ]

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

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
		{'title': 'Заголовок', 'format': 'h2'},
		{'title': 'Подзаголовок', 'format': 'h3'},
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
	'carousel': {'verbose_name': 'Для карусели (1080px)', 'width': 1080, 'height': '', 'opts': ''},
}
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail']
FILEBROWSER_EXTENSIONS = {
	'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp', '.webp'],
	'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv'],
	'Video': [],
	'Audio': []
}

GRAPPELLI_INDEX_DASHBOARD = 'tafos.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = 'Введенский храм'
GRAPPELLI_CLEAN_INPUT_TYPES = False



