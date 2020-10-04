from django.urls import path
from .views import *
from availability.views import AvailabilityListAPIView,AvailabilityDetailAPIView


urlpatterns = [
	path('', ProviderListAPIView.as_view(), name="create provider"),
	path('<int:pk>/', ProviderDetailAPIView.as_view(), name="prodiver detail"),
	path('<int:pk>/services/', ProviderServiceListAPIView.as_view(), name='service create'),
    path('<int:pk>/services/<int:service_id>/', ProviderServiceDetailAPIView.as_view(), name='service detail'),
    path('<int:provider_id>/services/<int:service_id>/availability/', AvailabilityListAPIView.as_view(), name='availability list'),
    path('<int:provider_id>/services/<int:service_id>/availability/days/<int:day_id>/', AvailabilityDetailAPIView.as_view(), name='availability detail'),

]














