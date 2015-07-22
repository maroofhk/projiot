from rest_framework import serializers

from device.models import *

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('pk', 'device_name', 'type', 'location', 'active')
        
class NurseSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True)
    
    class Meta:
        model = Nurse
        fields = ('pk', 'first_name', 'last_name', 'devices', 'hospital_assignment', 'qualification')
