from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CategorySerializer, ServiceTypeSerializer, ServiceSerializer
from .models import Category, ServiceType, Service


class CategoryListAPIView(APIView):
	"""
    get:
    Return a list of all the existing categories.

    post:
    Create a new category instance.
    """
	def post(self, request, format=None):
		serializer = CategorySerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)

	def get(self, request, format=None):
		categories = Category.objects.all()
		serializer = CategorySerializer(categories, many=True)
		return Response(serializer.data)


class CategoryDetailAPIView(APIView):
	"""
		get:
		Return a category instance.

		delete:
		Remove an existing category.

		put:
		Update a category.
	"""

	def get_object(self, pk):
		try:
			return Category.objects.get(pk=pk)
		except Category.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
		category = self.get_object(pk)
		serializer = CategorySerializer(category, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)


	def get(self, request, pk, format=None):
		category = self.get_object(pk)
		serializer = CategorySerializer(category)
		return Response(serializer.data)


	def delete(self, request, pk, format=None):
		category = self.get_object(pk)
		category.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceTypeListAPIView(APIView):
	"""
	post:
    Create a new service types instance.

    get:
    Return a list of all the existing service types.

    """

	def post(self, request, format=None):
		serializer = ServiceTypeSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)

	def get(self, request, format=None):
		service_types = ServiceType.objects.all()
		serializer = ServiceTypeSerializer(service_types, many=True)
		return Response(serializer.data)


class ServiceTypeDetailAPIView(APIView):
	"""
		get:
		Return a service type instance.

		delete:
		Remove an existing service type.

		put:
		Update a service type.
	"""
	def get_object(self, pk):
		try:
			return ServiceType.objects.get(pk=pk)
		except ServiceType.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
		service_type = self.get_object(pk)
		serializer = ServiceTypeSerializer(service_type, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)


	def get(self, request, pk, format=None):
		service_type = self.get_object(pk)
		serializer = ServiceTypeSerializer(service_type)
		return Response(serializer.data)


	def delete(self, request, pk, format=None):
		service_type = self.get_object(pk)
		service_type.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceListAPIView(APIView):
	"""
	post:
    Create a new service  instance.

    get:
    Return a list of all the existing services.

    """
	def post(self, request, format=None):
		serializer = ServiceSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)

	def get(self, request, format=None):
		services = Service.objects.all()
		serializer = ServiceSerializer(services, many=True)
		return Response(serializer.data)


class ServiceDetailAPIView(APIView):
	"""
		get:
		Return a service instance.

		delete:
		Remove an existing service .

		put:
		Update a service .
	"""
	def get_object(self, pk):
		try:
			return Service.objects.get(pk=pk)
		except Service.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
		service = self.get_object(pk)
		serializer = ServiceSerializer(service, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)


	def get(self, request, pk, format=None):
		service = self.get_object(pk)
		serializer = ServiceSerializer(service)
		return Response(serializer.data)


	def delete(self, request, pk, format=None):
		service = self.get_object(pk)
		service.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)