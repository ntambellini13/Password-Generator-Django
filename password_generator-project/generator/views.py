from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    generatedPassword = ''

    for x in range(length):
        generatedPassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generatedPassword})