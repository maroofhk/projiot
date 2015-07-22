from django.db import models

class Device(models.Model):
    device_name = models.CharField(max_length=100) # dev1, dev2, ...
    type = models.CharField(max_length=30) # fall, weight, heart, IV, ....
    location = models.CharField(max_length=100) # location1, location2, ...
    active = models.BooleanField(max_length=5) # true/false
    
    def __str__(self):
        return self.device_name
    
class Nurse(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    devices = models.ManyToManyField(Device, blank=True)
    hospital_assignment = models.CharField(max_length=100) # hospital1, hospital2, hospital3, ...
    qualification = models.CharField(max_length=100, blank=True) # administer medicine, CPR, ...
    
    def __str__(self):
        return '{l}, {f}'.format(l=self.last_name, f=self.first_name)
        #return self.devices
