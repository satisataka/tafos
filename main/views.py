from django.views.generic import ListView
from nav.models import MenuItem, Menu


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
			context['active_menu'] = {'name': active_menu.name}
		return context
