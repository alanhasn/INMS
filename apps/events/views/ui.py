from django.shortcuts import render

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from apps.devices.models import Device
from apps.events.models import Event

def test(request):
    # --- 1. Data for Summary Cards (last 24 hours) ---
    twenty_four_hours_ago = timezone.now() - timedelta(days=1)
    
    # Query the counts for each severity level
    critical_count = Event.objects.filter(
        severity=Event.SavertyChoices.CRITICAL, 
        event_date__gte=twenty_four_hours_ago
    ).count()

    warning_count = Event.objects.filter(
        severity=Event.SavertyChoices.WARNING, 
        event_date__gte=twenty_four_hours_ago
    ).count()
    
    error_count = Event.objects.filter(
        severity=Event.SavertyChoices.ERROR,
        event_date__gte=twenty_four_hours_ago
    ).count()

    info_count = Event.objects.filter(
        severity=Event.SavertyChoices.INFO, 
        event_date__gte=twenty_four_hours_ago
    ).count()
    
    # --- 2. Data for the Events Table ---
    # Get all events, which are already ordered by date due to the model's Meta class
    all_events = Event.objects.select_related('device').all()
    
    # --- 3. Data for the 'Add Event' Modal ---
    all_devices = Device.objects.all()

    context = {
        'active_page': 'events',
        'critical_count': critical_count,
        'warning_count': warning_count,
        'error_count': error_count,
        'info_count': info_count,
        'events': all_events,
        'devices': all_devices,
    }
    return render(request, 'events/events.html', context)