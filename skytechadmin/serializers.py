from rest_framework import serializers
from .models import *


class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservicename
        fields = ('main_service_name','service_name', 'about_service')