from django.shortcuts import render

def test(request):
    context = {
        'active_page': 'events'      # <-- to highlight the sidebar link
    }
    return render(request, "events/events.html" , context)
