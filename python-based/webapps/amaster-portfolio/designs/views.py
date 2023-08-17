from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Designs')

def uno(request):
    return HttpResponse('Uno design')
