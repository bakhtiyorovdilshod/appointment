from django.urls import path
from .views import *


urlpatterns = [
	path('', CustomerListAPIView.as_view(), name="create customer"),
	path('<int:pk>/', CustomerDetailAPIView.as_view(), name="customer detail"),
	
    
]
