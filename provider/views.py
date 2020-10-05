from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from provider.models import Provider
from .serializers import ProviderSerializer
from service.models import Service
User = get_user_model()
from service.serializers import ServiceSerializer
	

class ProviderListAPIView(APIView):
	"""
    get:
    Return a list of all the existing providers.

    post:
    Create a new provider instance.
    """

	def post(self, request, format=None):
		data = request.data
		data['user'] = request.user.id
		user = User.objects.filter(id=data['user']).first()
		user.is_provider = True
		user.save()
		serializer = ProviderSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)

	def get(self, request, format=None):
		providers = Provider.objects.all()
		serializer = ProviderSerializer(providers, many=True)
		return Response(serializer.data)


class ProviderDetailAPIView(APIView):
	"""
		get:
		Return a provider instance.

		delete:
		Remove an existing provider.

		put:
		Update a provider.
	"""
	def get_object(self, pk):
		try:
			return Provider.objects.get(pk=pk)
		except Provider.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
		data = request.data
		user = request.user.id
		provider = self.get_object(pk)
		data['user'] = user 
		serializer = ProviderSerializer(provider, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)


	def get(self, request, pk, format=None):
		provider = self.get_object(pk)
		serializer = ProviderSerializer(provider)
		return Response(serializer.data)


	def delete(self, request, pk, format=None):
		provider = self.get_object(pk)
		provider.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class ProviderServiceListAPIView(APIView):
	"""
	post:
    Create a new provider service instance.

    get:
    Return a list of all the existing provider's services
  
    """



	def get_object(self, pk):
		try:
			return Provider.objects.get(pk=pk)
		except Provider.DoesNotExist:
			raise Http404

	def post(self, request, pk, format=None):
		provider = self.get_object(pk)
		data = request.data
		data['provider']=provider.id
		serializer = ServiceSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		service_id = serializer.data['id']
		get_service = Service.objects.get(pk=service_id)
		provider.services.add(get_service)
		return Response(data=serializer.data)

	def get(self, request, pk, format=None):
		provider = self.get_object(pk)
		serializer = ProviderSerializer(provider, many=False)
		services = serializer.data['services']
		return Response(services)


class ProviderServiceDetailAPIView(APIView):

	"""
		get:
		Return a provider service instance.

		delete:
		Remove an existing provider service.

		put:
		Update a provider service.
	"""

	def get_provider(self, pk):
		try:
			return Provider.objects.get(pk=pk)
		except Provider.DoesNotExist:
			raise Http404

	def get_service(self, pk):
		try:
			return Service.objects.get(pk=pk)
		except Service.DoesNotExist:
			raise Http404

	def put(self, request, pk, service_id, format=None):
		data = request.data
		service = self.get_service(service_id)
		provider = self.get_provider(pk)
		data['provider'] = provider.id
		serializer = ServiceSerializer(service, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)


	def get(self, request, pk, service_id, format=None):
		service = self.get_service(service_id)
		serializer = ServiceSerializer(service)
		return Response(serializer.data)


	def delete(self, request, pk, service_id, format=None):
		service = self.get_provider(service_id)
		service.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)





