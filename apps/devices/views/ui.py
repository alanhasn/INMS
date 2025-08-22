from django.shortcuts import render
from ..forms import DeviceForm
from ...users.models import Profile

def test(request):
    profile  = Profile.objects.get(user=request.user) # Get the user profile
    context = {
        "profile": profile # -> User Profile Info
    }
    return render(request , "devices/devices.html" , context) 

