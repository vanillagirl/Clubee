from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Club
from django.contrib.auth.decorators import login_required

def principal(request):
    clubes = Club.objects.all()
    return render(request, 'Clubee/principal.html', {'clubes': clubes})

def lista(request):
    clubes = Club.objects.all()
    return render (request, 'Clubee/lista.html', {'clubes': clubes})

def login(request):
    return render (request, 'Clubee/login.html', {})

def clubdetalle(request, pk):
    clubes = get_object_or_404(Club, pk=pk)
    return render(request, 'Clubee/clubdetalle.html', {'clubes': clubes})
