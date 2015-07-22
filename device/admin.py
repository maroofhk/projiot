from django.contrib import admin

from device.models import *

class DeviceAdmin(admin.ModelAdmin):
    pass

class NurseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Device, DeviceAdmin)
admin.site.register(Nurse, NurseAdmin)