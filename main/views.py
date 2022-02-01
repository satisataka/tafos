from re import template
from django.shortcuts import render
from django.views.generic import ListView
from nav.models import MenuItem, Menu


def static_page(request, menu=None, sub_menu=None):
	"""
	link generation to static page
	"""
	if menu:
		name = menu
		if sub_menu:
			name += '/' + sub_menu
	return render(request, 'main/' + name + '.html')


class MenuItemView(ListView):
	model = MenuItem
	context_object_name = 'menu_items'

	def get_queryset(self):
		qs = self.model.objects.all()
		if self.kwargs.get('menu'):
			qs = qs.filter(menu__slug=self.kwargs['menu'])
		return qs

	def get_context_data(self, **kwargs):
		context = super(MenuItemView, self).get_context_data(**kwargs)
		if self.kwargs.get('menu'):
			active_menu = Menu.objects.get(slug=self.kwargs['menu'])
			context['active_menu'] = {'name': active_menu.name }
		return context
