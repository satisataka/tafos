from nav.models import Menu, MenuItem
from django import template
from django.core.cache import cache


register = template.Library()


def build_menu(parser, token):
	"""
	{% menu %}
	"""
	return MenuObject()


class MenuObject(template.Node):
	def render(self, context):
		try:
			current_path = context['request'].path
			user = context['request'].user
		except KeyError:
			current_path = None
			user = None

		context['menuitems'] = get_items(current_path)
		return ''


def get_items(current_path):
	"""
	If possible, use a cached list of items to avoid continually re-querying
	the database.
	The key contains the menu name, whether the user is authenticated, and the current path.
	Disable caching by setting MENU_CACHE_TIME to -1.
	"""
	from django.conf import settings
	cache_time = getattr(settings, 'MENU_CACHE_TIME', 1800)
	debug = getattr(settings, 'DEBUG', False)

	if cache_time >= 0 and not debug:
		cache_key = 'django-menu-items/%s/%s/%s' % (current_path)
		menuitems = cache.get(cache_key, [])
		if menuitems:
			return menuitems
	else:
		menuitems = []

	all_menu = Menu.objects.all().filter(hide=False).order_by('order')
	if not all_menu:
		return []

	for menu in all_menu:
		menu_list = []
		for i in MenuItem.objects.filter(menu=menu, hide=False).order_by('order'):
			'''if current_path:
				current = ( i.url != '/' and current_path.startswith(i.url)) or ( i.url == '/' and current_path == '/' )
				if menu.url and i.url == menu.url and current_path != i.url:
					current = False
			else:
				current = False'''
			'''url = i.url
			if i.url[0] == '/':
				url = menu.url + i.url[1:]'''
			menu_list.append({'slug': i.slug, 'title': i.title})
		menuitems.append({'menu_name': menu.name, 'menu_slug': menu.slug, 'menu_item': menu_list})

	if cache_time >= 0 and not debug:
		cache.set(cache_key, menuitems, cache_time)
	return menuitems


register.tag('menu', build_menu)
