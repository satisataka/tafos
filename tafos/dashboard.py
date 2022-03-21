"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
	GRAPPELLI_INDEX_DASHBOARD = 'tafos.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
	"""
	Custom index dashboard for www.
	"""
	title = "Тест"

	def init_with_context(self, context):
		site_name = get_admin_site_name(context)

		if context['request'].user.is_superuser:
			# append an app list module for "Applications"
			self.children.append(modules.AppList(
				_('Приложения'),
				collapsible=True,
				column=1,
				css_classes=('collapse closed',),
				exclude=('django.contrib.*',),
			))
			# append an app list module for "Administration"
			self.children.append(modules.AppList(
				_('Административные настройки'),
				column=2,
				collapsible=True,
				models=('django.contrib.*',),
			))

			self.children.append(modules.LinkList(
				title='Менеджер файлов',
				column=1,
				collapsible=False,
				children=[
					{
						'title': _('FileBrowser'),
						'url': '/admin/filebrowser/browse/',
						'external': False,
					},
				]
			))

			self.children.append(modules.RecentActions(
				_('Recent actions'),
				limit=10,
				collapsible=False,
				column=3,
			))
		else:
			self.children.append(modules.ModelList(
				collapsible=False,
				title='Новости Обители',
				column=1,
				models=('articles.models.Article', 'articles.models.Rubric', 'articles.models.Author')
			))
			self.children.append(modules.ModelList(
				collapsible=False,
				title='Рассписание',
				column=1,
				models=('timetable.*',)
			))
			self.children.append(modules.ModelList(
				collapsible=False,
				title='Карусель (Главная страница)',
				column=1,
				models=('main.models.СarouselMaster',)
			))
			self.children.append(modules.LinkList(
				title='Менеджер файлов',
				column=1,
				collapsible=False,
				children=[
					{
						'title': _('FileBrowser'),
						'url': '/admin/filebrowser/browse/',
						'external': False,
					},
				]
			))
			self.children.append(modules.RecentActions(
				_('Recent actions'),
				limit=10,
				collapsible=False,
				column=2,
			))
