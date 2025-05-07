from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def menu(request):
    return render(request, 'menu.html')  

def veiculos(request):
    return render(request, 'veiculos.html')

def home(request):
    return HttpResponse("Página inicial do site.")

@login_required
def menu(request):
    return render(request, 'menu.html')