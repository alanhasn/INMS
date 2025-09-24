from django.shortcuts import render

from ..models.report import Report
from apps.devices.models import Device

# Create your views here.

def test(request):
    all_reports = Report.objects.all()
    all_devices = Device.objects.all()
    context = {
        'active_page': 'reports',     # <-- to highlight the sidebar link
        'devices': all_devices,
        "reports": all_reports,
    }
    return render(request , "reports.html" , context)