from django.shortcuts import render


def static_page(request, menu=None, sub_menu=None):
	"""
	link generation to static page
	"""
	if menu:
		name = menu
		if sub_menu:
			name += '/' + sub_menu
	return render(request, 'main/' + name + '.html')
