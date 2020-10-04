"""make_appointment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Appointment API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view, name="docs"),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/service/', include('service.urls')),
    path('api/v1/provider/', include('provider.urls')),
    path('api/v1/availability/', include('availability.urls')),
    path('api/v1/customer/', include('customer.urls'))

]