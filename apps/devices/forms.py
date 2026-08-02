from django import forms
from django.contrib.auth import get_user_model

from .models import Device

INPUT_CLASSES = "w-full bg-slate-700 border border-slate-600 rounded-lg px-3 py-2 focus:ring-2 focus:ring-cyan-500 text-slate-200"


class DeviceForm(forms.ModelForm):
    owner = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        label="Assign To",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
    )

    class Meta:
        model = Device
        fields = [
            'device_name',
            'device_type',
            'ip_address',
            'mac_address',
            'location',
            'status',
            'owner',
            'description',
            ]

        widgets = {
            'device_name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'device_type': forms.Select(attrs={'class': INPUT_CLASSES}),
            'ip_address': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'mac_address': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'location': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES, 'rows': 3}),
            'status': forms.Select(attrs={'class': INPUT_CLASSES}),
        }