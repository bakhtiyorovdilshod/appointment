from rest_framework.views import APIView
from .serializers import AvailabilitySerializer,UpdateWorkingDaySerializer,AddBreakSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Availability
from provider.models import Provider
from service.models import Service
from django.http import Http404


class AvailabilityListAPIView(APIView):
	"""
	post:
    Create a new week day instance.

    get:
    Return a list of all the existing week days.
    """

	def get_provider(self, pk):
		try:
			return Provider.objects.get(pk=pk)
		except Provider.DoesNotExist:
			raise Http404


	def post(self, request, provider_id, format=None):
		data = request.data
		provider = self.get_provider(provider_id).id
		data['provider'] = provider
		serializer = AvailabilitySerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)

	def get(self, request, provider_id, format=None):
		provider = self.get_provider(provider_id).id
		availability = Availability.objects.filter(provider=provider)
		serializer = AvailabilitySerializer(availability, many=True)
		return Response(serializer.data)


class AvailabilityDetailAPIView(APIView):
	"""
		get:
		Return a week day instance.

		delete:
		Remove an existing week day.

		put:
		Update a week day.
	"""

	def get_provider(self, provider_id):
		try:
			return Provider.objects.get(pk=provider_id)
		except Provider.DoesNotExist:
			raise Http404

	def get_day(self, day_id):
		try:
			return Availability.objects.get(pk=day_id)
		except Availability.DoesNotExist:
			raise Http404




	def put(self, request, provider_id, day_id, format=None):
		data = request.data
		provider_id = self.get_provider(provider_id).id
		day_id = self.get_day(day_id).id
		availability_qs = Availability.objects.filter(pk=day_id, provider=provider_id).first()
		data['provider']= provider_id
		serializer = AvailabilitySerializer(availability_qs, data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)

	def get(self, request, provider_id,day_id, format=None):
		provider_id = self.get_provider(provider_id).id
		day_id = self.get_day(day_id).id
		availability_qs = Availability.objects.filter(pk=day_id, provider=provider_id).first()
		serializer = AvailabilitySerializer(availability_qs)
		return Response(serializer.data)

	def delete(self, request, provider_id, day_id, format=None):
		data = request.data 
		provider_id = self.get_provider(provider_id).id
		day_id = self.get_day_id(day_id).id
		week_day = Week.objects.filter(pk=day_id, provider=provider_id).first()
		week_day.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class UpdateWorkingDayAPIView(APIView):

	def get_provider(self, provider_id):
		try:
			return Provider.objects.get(pk=provider_id)
		except Provider.DoesNotExist:
			raise Http404

	def get_day(self, day_id):
		try:
			return Availability.objects.get(pk=day_id)
		except Availability.DoesNotExist:
			raise Http404

	def put(self, request, provider_id, day_id):
		data = request.data
		provider_id = self.get_provider(provider_id).id
		day_id = self.get_day(day_id).id
		availability_qs = Availability.objects.filter(pk=day_id, provider=provider_id).first()
		serializer = UpdateWorkingDaySerializer(availability_qs, data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)








