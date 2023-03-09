from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tvs(request):
    return HttpResponse('<h1>In TVS Apachi one and only Racing Bike</h1>')

def bajaj(request):
    return HttpResponse('<h1>In Bajaj company most selling is pular Ns200</h1>')
