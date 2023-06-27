from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import AccelViewSet

router = routers.DefaultRouter()
router.register(r'accel', AccelViewSet)    

urlpatterns = [
    path('',include(router.urls))]