from django.db import models
from provider.models import Provider
from service.models import Category, ServiceType, Service


class Availability(models.Model):
	days = [
		('monday', 'm'),
		('tuesday', 't'),
		('wednesday', 'w'),
		('thursday', 'th'),
		('friday', 'f'),
		('saturday', 's'),
		('sunday', 'su'),
	]
	day = models.CharField(max_length=20, choices=days, default=None)
	begin = models.TimeField(blank=True, null=True)
	end = models.TimeField(blank=True, null=True)
	is_break = models.BooleanField(default=False)
	is_working = models.BooleanField(default=True, blank=True, null=True)
	provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
	date = models.DateField(blank=True, null=True)
	

	def __str__(self):
		return str(self.id)
