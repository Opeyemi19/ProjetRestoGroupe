from django.shortcuts import render

# Create your views here.


def home(request):
    data = {}
    return render(request,"pages/restaurant/index.html")


def Menu(request):
    data = {}
    return render(request,"pages/restaurant/menu.html")

def jours(request):
    data = {}
    return render(request,"pages/restaurant/jours.html")


def About(request):
    data = {}
    return render(request,"pages/restaurant/about.html")


def specialite(request):
    data = {}
    return render(request,"pages/restaurant/specialite.html")