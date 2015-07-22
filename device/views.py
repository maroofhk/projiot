from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from device.serializers import *
from device.models import Device, Nurse

from device.forms import DeviceForm, NurseForm
# from device.forms import DeviceForm

# --------------------- login added
from django.contrib.auth import authenticate, login, logout
from projiot import settings
from django.contrib.auth.decorators import login_required
# --------------------- login added

# --------------------- login added
@login_required
# --------------------- login added
@api_view(['GET'])
def all_devices(request, **kwargs):
    devices = Device.objects.all()
    
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

# --------------------- login added
@login_required
# --------------------- login added
@api_view(['GET'])
def all_nurses(request, **kwargs):
    nurses = Nurse.objects.all()
    
    serializer = NurseSerializer(nurses, many=True)
    return Response(serializer.data)

# --------------------- login added
@login_required
# --------------------- login added    
@api_view(['POST'])
def update_device_state(request, **kwargs):
    device = Device.objects.get(pk=request.data['device_pk'])
    device_state = request.data['device_state']
    device_state = bool(device_state)
    
    device.active = device_state
    device.save(update_fields=['active'])
    
    serializer = DeviceSerializer(device)
    return Response(serializer.data)

# --------------------- login added
@login_required
# --------------------- login added
def nurse_list(request):
    nurse_list = Nurse.objects.all()
    
    context = {'nurse_list': nurse_list}
    return render(request, 'device/nurse_list_del.html', context)
    #return render(request, 'device/nurse_list.html', context)

# --------------------- login added
@login_required
# --------------------- login added 
def device_list(request):
    device_list = Device.objects.all().order_by('active').order_by('location')
    
    context = {'device_list': device_list}
    return render(request, 'device/device_list.html', context)

# --------------------- login added
@login_required
# --------------------- login added
def device_details(request, pk):
    device_at_id = Device.objects.get(pk=pk)

    nurseList = []
    for nurse in Nurse.objects.all():
        for dev in nurse.devices.all():
            dev_str = str(dev)
            if dev_str == str(device_at_id):
                nurseList.append(Nurse.objects.get(pk=nurse.id))
    #context = {'id': pk, 'device_at_id': device_at_id, 'list_id': list_id, 'list_name': list_name}
    context = {'device_at_id':device_at_id, 'nurseList': nurseList}
    return render(request, 'device/device_details.html', context)

# --------------------- login added
@login_required
# --------------------- login added    
def home(request): # this is used to add a device
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        device_name = form.cleaned_data['device_name']
        type = form.cleaned_data['type']
        location = form.cleaned_data['location']
        active = form.cleaned_data['active']
        new_device, created = Device.objects.get_or_create(device_name=device_name, type=type, location=location, active=active)
        if created:
            new_device.save()
        return HttpResponseRedirect("/%s was added."%(new_device.device_name))
        
    context = {'form': form}
    return render(request, 'device/home.html', context)
    
# --------------------- login added
@login_required
# --------------------- login added
def add_nurse(request):
    form = NurseForm(request.POST or None)
    if form.is_valid():
        #new_nurse = form.save(commit=False)
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        devices = Device.objects.get(pk=form.cleaned_data['devices'])#form.cleaned_data['devices']
        print('---------------------------', form.cleaned_data['devices'])
        hospital_assignment = form.cleaned_data['hospital_assignment']
        qualification = form.cleaned_data['qualification']
        #new_nurse, created = Nurse.objects.get_or_create(first_name=first_name, last_name=last_name, devices=devices, hospital_assignment=hospital_assignment, qualification=qualification)
        new_nurse, created = Nurse.objects.get_or_create(first_name=first_name, last_name=last_name, hospital_assignment=hospital_assignment, qualification=qualification)
        if created:
            #new_nurse.save_m2m()
            new_nurse.save()
            new_nurse.devices.add(devices)
        return HttpResponseRedirect("/%s was added."%(new_nurse.first_name))
        
    context = {'form': form}
    return render(request, 'device/add_nurse.html', context)
