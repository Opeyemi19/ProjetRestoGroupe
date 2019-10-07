from django.shortcuts import render

# Create your views here.

def team(request):
    data = {}
    return render(request,"pages/personelle/team.html")