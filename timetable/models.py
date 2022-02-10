from django.db import models


class ListChurchService(models.Model):
	name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
	hide = models.BooleanField(verbose_name='Скрыть', default=False)

	class Meta:
		verbose_name_plural = 'Церковные службы'
		verbose_name = ''
		ordering = ['name']

	def __str__(self):
		return self.name


class TimeTable(models.Model):
	day = models.DateField(db_index=True, unique=True, verbose_name='Дата', help_text='Введите дату')

	class Meta:
		verbose_name = ''
		verbose_name_plural = 'Расписание'
		ordering = ['day']

	def day_of_week(self):
		RUSSIAN_DAY_WEEK_CHOOSE = {
			0: 'Понедельник',
			1: 'Вторник',
			2: 'Среда',
			3: 'Четверг',
			4: 'Пятница',
			5: 'Суббота',
			6: 'Воскресенье',
		}
		return RUSSIAN_DAY_WEEK_CHOOSE[self.day.weekday()]

	day_of_week.short_description = "День недели"

	def save(self, *args, **kwargs):
		print(self.day_of_week())
		super(TimeTable, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.day.strftime("%d.%m.%y")) + ' (' + self.day_of_week() + ')'


class TimeTableItem(models.Model):
	date = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
	time = models.TimeField(blank=False, verbose_name='Время', null=True)
	service = models.ForeignKey(ListChurchService, on_delete=models.PROTECT, default='', verbose_name='Выберете службу')
	text = models.TextField(blank=True, verbose_name='Дополнительная информация')

	def __str__(self):
		return self.service.name + ' (' + self.time.strftime("%H:%M") + ')'

	class Meta:
		verbose_name_plural = 'Богослужения'
		verbose_name = 'Богослужение'
		ordering = ['date', 'time']