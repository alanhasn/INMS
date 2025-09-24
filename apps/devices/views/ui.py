from django.core.paginator import Paginator  # <-- IMPORT THE PAGINATOR
from django.shortcuts import render

# Import the necessary models
from apps.devices.models import Device
from apps.events.models import Event

from ...users.models import Profile
from ..forms import DeviceForm


def test(request):
    # Get the full list of devices. We can add optimizations like prefetching related data later.
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
    }
    return render(request, 'devices/devices.html', context) 