from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h1>King kohli done 50th century</h1>')

def msd(request):
    return HttpResponse('<h1>MR.COOL</h1>')