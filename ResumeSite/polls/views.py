from django.shortcuts import render
from django.views.generic.base import View

def index(request):
    return render(request, 'index.html')
