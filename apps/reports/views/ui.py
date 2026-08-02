from django.shortcuts import render

from ..models.report import Report
from apps.devices.models import Device
from apps.users.models import CustomUser
from apps.users.permissions.user_permissions import role_required

# Create your views here.

@role_required(CustomUser.Roles.ADMIN, CustomUser.Roles.Manager)
def test(request):
    all_reports = Report.objects.all()
    all_devices = Device.objects.all()
    context = {
        'active_page': 'reports',     # <-- to highlight the sidebar link
        'devices': all_devices,
        "reports": all_reports,
    }
    return render(request , "reports.html" , context)