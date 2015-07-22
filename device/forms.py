from django import forms

from .models import Device, Nurse

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_name', 'type', 'location', 'active']

# ---------------- new addition
class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        #fields = ['first_name', 'last_name', 'devices', 'hospital_assignment', 'qualification']
        #fields = ['first_name', 'last_name', 'hospital_assignment', 'qualification']
# ---------------- new addition