from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def letter(request):
    return render(request, "letter.html")

# Create your views here.
