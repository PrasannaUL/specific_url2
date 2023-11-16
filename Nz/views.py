from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def williomson(request):
    return HttpResponse('<h1>well played</h1>')

def shreyas(request):
    return HttpResponse('<h1>Try to do century</h1>')