from django.shortcuts import render

def track_view(request):
    return render(request, 'track.html')