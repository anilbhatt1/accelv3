from django.shortcuts import render
from rest_framework import viewsets
from api.models import Accel
from api.serializers import AccelSerializer

# Create your views here.
class AccelViewSet(viewsets.ModelViewSet):
    queryset = Accel.objects.all()
    serializer_class = AccelSerializer