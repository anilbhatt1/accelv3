from rest_framework import serializers
from api.models import Accel

class AccelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accel
        fields="__all__"