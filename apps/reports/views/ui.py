from django.shortcuts import render , HttpResponse

# Create your views here.

def test(request):
    return render(request , "reports.html")