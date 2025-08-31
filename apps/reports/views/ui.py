from django.shortcuts import render

from ..models.report import Report

# Create your views here.

def test(request):
    all_reports = Report.objects.all()
    context = {
        'active_page': 'reports' ,     # <-- to highlight the sidebar link
        "reports": all_reports,
    }
    return render(request , "reports.html" , context)