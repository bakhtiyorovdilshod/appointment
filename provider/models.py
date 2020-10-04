from django.db import models
from django.contrib.auth import get_user_model
from user.models import Contact
from service.models import Service

User = get_user_model()


class Provider(models.Model):
	gender = [
		('male', 'male'),
		('female', 'female')
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	gender = models.CharField(max_length=6, choices=gender, default=None, blank=True, null=True)
	rate = models.IntegerField(default=0,blank=True, null=True)
	contacts = models.ManyToManyField(Contact)
	services = models.ManyToManyField(Service)
	objects = models.Manager()

	def __str__(self):
		return str(self.user)