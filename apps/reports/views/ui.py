from django.shortcuts import render , HttpResponse

# Create your views here.

def test(request):
    context = {
        'active_page': 'reports'      # <-- to highlight the sidebar link
    }
    return render(request , "reports.html" , context)