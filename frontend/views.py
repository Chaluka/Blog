from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, *args, **kargs):
    return render(request, 'frontend/index.html')
