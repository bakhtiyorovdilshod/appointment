from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Customer
from .serializers import CustomerSerializer
from service.models import Service
User = get_user_model()



class CustomerListAPIView(APIView):

	"""
	post:
    Create a new customer  instance.

    get:
    Return a list of all the existing customers
  
    """


	def post(self, request, format=None):
		data = request.data
		data['user'] = request.user.id
		user = User.objects.filter(id=data['user']).first()
		user.is_provider = False
		user.save()
		serializer = CustomerSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)

	def get(self, request, format=None):
		customers = Provider.objects.all()
		serializer = ProviderSerializer(customers, many=True)
		return Response(serializer.data)


class CustomerDetailAPIView(APIView):

	"""
		get:
		Return a cutomer instance

		delete:
		Remove an existing customer

		put:
		Update a customer
	"""

	def get_object(self, pk):
		try:
			return Customer.objects.get(pk=pk)
		except Customer.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
		data = request.data
		user = request.user.id
		customer = self.get_object(pk)
		data['user'] = user 
		serializer = CustomerSerializer(customer, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(data=serializer.data)


	def get(self, request, pk, format=None):
		customer = self.get_object(pk)
		serializer = CustomerSerializer(customer)
		return Response(serializer.data)


	def delete(self, request, pk, format=None):
		customer = self.get_object(pk)
		customer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)





	