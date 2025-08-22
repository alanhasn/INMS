from django.shortcuts import render
from ..forms import DeviceForm

def test(request):
    return render(request , "devices/devices.html") 

def add_devices(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        devices = form.save(commit=False)
        devices.owner = request.user
        devices.save()
    else:
        form = DeviceForm()
    context = {
        "form": form,
    }
    return render(request, "devices/devices.html", context=context)