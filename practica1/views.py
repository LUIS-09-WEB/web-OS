from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html",)

# Create your views here.
def servicios(request):
    return render(request,"servicios.html",)

def contactos(request):
    return render(request,"contactos.html",)
