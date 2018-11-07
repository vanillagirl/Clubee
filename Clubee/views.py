from django.shortcuts import render
from django.utils import timezone
from .models import Club

def principal(request):
    clubes = Club.objects.all()
    return render(request, 'Clubee/principal.html', {})
