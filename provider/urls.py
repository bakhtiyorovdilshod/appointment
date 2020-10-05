from django.urls import path
from .views import *
from availability.views import *


urlpatterns = [
	path('', ProviderListAPIView.as_view(), name="create provider"),
	path('<int:pk>/', ProviderDetailAPIView.as_view(), name="prodiver detail"),
	path('<int:pk>/services/', ProviderServiceListAPIView.as_view(), name='service create'),
    path('<int:pk>/services/<int:service_id>/', ProviderServiceDetailAPIView.as_view(), name='service detail'),
    path('<int:provider_id>/availability/', AvailabilityListAPIView.as_view(), name='availability list'),
    path('<int:provider_id>/availability/day/<int:day_id>/', AvailabilityDetailAPIView.as_view(), name='availability detail'),
    path('<int:provider_id>/availability/change/<int:day_id>/', UpdateWorkingDayAPIView.as_view(), name='update day'),

]














