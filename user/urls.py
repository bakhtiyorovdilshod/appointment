from django.urls import path
from .views import *


urlpatterns = [
	path("register/", Phone_VerificationAPIView.as_view(), name="register"),
	path("verification/", Token_ValidationAPIView.as_view(), name="verification"),
	path("sigin/", LoginAPIView.as_view(), name="sigin")
    
]