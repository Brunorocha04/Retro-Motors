from django.shortcuts import render
from django.http import HttpResponse

def viaturas_views(request):
    return render(request, 'viaturas.html')
