from nav.models import Menu, MenuItem
from django import template
from django.core.cache import cache


register = template.Library()


def build_breadcrumbs(parser, token):
	"""
	{% breadcrumbs %}
	"""
	return BreadCrumbsObject()


class BreadCrumbsObject(template.Node):
	def render(self, context):
		current_path = context['request'].path[1:]
		menu = False
		menu_item = False
		context['crumbs'] = []

		if current_path:
			for m in Menu.objects.filter(slug__isnull=False):
				if m.slug and current_path.startswith(m.slug):
					menu = m

			if menu:
				current_path = current_path.replace(menu.slug + '/', '', 1)
				if current_path:
					for item in MenuItem.objects.filter(menu=menu):
						if item.slug and current_path.startswith(item.slug):
							menu_item = item
					if menu_item:
						current_path = current_path.replace(menu_item.slug + '/', '', 1)
						context['crumbs'] = [{'menu_slug': menu.slug, 'menu_name': menu.name, 'menu_item_slug': menu_item.slug, 'menu_item_name': menu_item.title, 'current_path': current_path}]
				else:
					context['crumbs'] = [{'menu_slug': menu.slug, 'menu_name': menu.name, 'current_path': current_path}]
			else:
				context['crumbs'] = [{'current_path': current_path}]
		return ''


register.tag('build_breadcrumbs', build_breadcrumbs)
