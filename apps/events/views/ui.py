from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator  # <-- IMPORT THE PAGINATOR
from apps.devices.models import Device
from apps.events.models import Event

def test(request):
    # --- 1. Data for Summary Cards (last 24 hours) ---
    twenty_four_hours_ago = timezone.now() - timedelta(days=1)
    
    critical_count = Event.objects.filter(severity=Event.SavertyChoices.CRITICAL, event_date__gte=twenty_four_hours_ago).count()
    warning_count = Event.objects.filter(severity=Event.SavertyChoices.WARNING, event_date__gte=twenty_four_hours_ago).count()
    error_count = Event.objects.filter(severity=Event.SavertyChoices.ERROR, event_date__gte=twenty_four_hours_ago).count()
    info_count = Event.objects.filter(severity=Event.SavertyChoices.INFO, event_date__gte=twenty_four_hours_ago).count()
    
    # --- 2. PAGINATED Data for the Events Table ---
    # First, get the full list of all events
    event_list = Event.objects.select_related('device').all()
    
    # Create a Paginator instance with 10 events per page
    paginator = Paginator(event_list, 10) 
    
    # Get the current page number from the GET request (e.g., /events/?page=2)
    page_number = request.GET.get('page')
    
    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)
    
    # --- 3. Data for the 'Add Event' Modal ---
    all_devices = Device.objects.all()

    context = {
        'active_page': 'events',
        'critical_count': critical_count,
        'warning_count': warning_count,
        'error_count': error_count,
        'info_count': info_count,
        'page_obj': page_obj,  # <-- PASS THE PAGE OBJECT, NOT THE FULL LIST
        'devices': all_devices,
    }
    return render(request, 'events/events.html', context)