from django.urls import path
from .views import *


urlpatterns = [
	path('service_type/', ServiceTypeListAPIView.as_view(), name="create service type"),
	path('service_type/<int:pk>/', ServiceTypeDetailAPIView.as_view(), name="service type detail"),
	path('category/', CategoryListAPIView.as_view(), name='category detail'),
	path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category detail')
]