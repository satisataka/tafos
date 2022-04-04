import os
from django.conf import settings
from PIL import ImageDraw, ImageFont


def water_marks_processor(im, water_marks=False, **kwargs):
	if water_marks:
		idraw = ImageDraw.Draw(im)
		text = "tafos.ru"
		font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'static/fonts/BalkaraFreeCondensed.ttf'), size=22)
		_, height = im.size
		position = (10, height - 29)
		try:
			idraw.text(position, text, font=font, fill='#d1ac77')
		except:
			pass
	return im
