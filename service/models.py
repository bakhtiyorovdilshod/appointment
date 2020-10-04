from django.db import models
# from provider.models import Provider


class ServiceType(models.Model):
	service_type = models.CharField(max_length=500)

	def __str__(self):
		return self.service_type


class Category(models.Model):
	name = models.CharField(max_length=500)
	service_types = models.ManyToManyField(ServiceType)

	def __str__(self):
		return self.name


class Service(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.category)


# class ServiceDetail(models.Model):
# 	service = models.ForeignKey(Service, on_delete=models.CASCADE)
# 	country = models.CharField(max_length=200)
# 	city = models.CharField(max_length=200)
	