from rest_framework import serializers
from .models import *

class MainserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainservice
        fields =('main_service_name',)

class SubserviceSerializer(serializers.ModelSerializer):
    main_service_name = MainserviceSerializer()
    class Meta:
        model = Subservicename
        fields = ('main_service_name','service_name', 'service_img','about_service')