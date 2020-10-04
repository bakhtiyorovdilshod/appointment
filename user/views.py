from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from phone_verification import client
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
User = get_user_model()



class Phone_VerificationAPIView(APIView):
	"""
		post:
		Register users.
	"""
	def post(self, request):
		data = request.data
		phone_number = data['phone_number']
		password = data['password']
		verification = client.verifications(phone_number)
		return Response("Code is sent your phone. Check it ")


class Token_ValidationAPIView(APIView):
	"""
		post:
		Phone Number Verification.
	"""
	def post(self, request):
		data = request.data
		token = data['token']
		phone_number = data['phone_number']
		password = data['password']
		verification = client.verification_checks(phone_number, token)
		if verification.status == 'approved':
			new_user = User.objects.create_user(phone_number, password)
			token, _ = Token.objects.get_or_create(user=new_user)
			return Response({'status':200})
		else:
			return Response({'status':404})


class LoginAPIView(APIView):
	"""
		post:
		Login users.
	"""
	def post(self, request):
		data = request.data
		phone_number = data['phone_number']
		password = data['password']
		user = authenticate(phone_number=phone_number, password=password)
		if not user:
			return Response({'error': 'Invalid Credentials'})
		else:
			token, _ = Token.objects.get_or_create(user=user)
			return Response({'token': token.key, 'user_id':user.id})
        