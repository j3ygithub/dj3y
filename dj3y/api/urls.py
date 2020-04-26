"""dj3y URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# the default import
from django.urls import path, include

# my import
from rest_framework import routers

# my import which may grow during adding new models
from crm.views import PersonViewSet
from crm.views import DeviceViewSet

# my code


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('person', PersonViewSet)
router.register('device', DeviceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('browser/', include(router.urls)),
    path('browser/', include('rest_framework.urls', namespace='rest_framework'))
]