from django.contrib import messages
from django.core.paginator import Paginator  # <-- IMPORT THE PAGINATOR
from django.shortcuts import get_object_or_404, redirect, render

# Import the necessary models
from apps.devices.models import Device
from apps.events.models import Event

from ...users.models import CustomUser, Profile
from ...users.permissions.user_permissions import role_required
from ..forms import DeviceForm


@role_required(CustomUser.Roles.ADMIN, CustomUser.Roles.Manager, CustomUser.Roles.Employee)
def test(request):
    # Admins/Managers oversee every device; Employees only see devices assigned to them.
    if request.user.role == CustomUser.Roles.Employee:
        device_list = Device.objects.filter(owner=request.user)
    else:
        device_list = Device.objects.all()

    # Create a Paginator instance with 15 devices per page (you can adjust this number)
    paginator = Paginator(device_list, 15) 
    
    # Get the current page number from the URL's GET parameters (e.g., /devices/?page=3)
    page_number = request.GET.get('page')
    
    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)
    
    context = {
        'active_page': 'devices',
        'devices': device_list,
        'page_obj': page_obj,  # <-- PASS THE PAGE OBJECT to the template
        'form': DeviceForm(),  # Empty form for the "Add Device" modal
    }
    return render(request, 'devices/devices.html', context)


@role_required(CustomUser.Roles.ADMIN, CustomUser.Roles.Manager)
def create_device(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Device added successfully.")
            return redirect("devices:devices")
        messages.error(request, "Please correct the errors below.")
        device_list = Device.objects.all()
        paginator = Paginator(device_list, 15)
        page_obj = paginator.get_page(request.GET.get('page'))
        context = {
            'active_page': 'devices',
            'devices': device_list,
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, 'devices/devices.html', context)
    return redirect("devices:devices")


@role_required(CustomUser.Roles.ADMIN, CustomUser.Roles.Manager)
def update_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, f"Device '{device.device_name}' updated successfully.")
            return redirect("devices:devices")
        messages.error(request, "Please correct the errors below.")
    else:
        form = DeviceForm(instance=device)
    return render(request, 'devices/device_edit.html', {'form': form, 'device': device, 'active_page': 'devices'})


@role_required(CustomUser.Roles.ADMIN, CustomUser.Roles.Manager)
def delete_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        device_name = device.device_name
        device.delete()
        messages.success(request, f"Device '{device_name}' deleted successfully.")
    return redirect("devices:devices")