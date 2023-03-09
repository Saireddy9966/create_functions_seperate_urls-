from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def honda(request):
    return HttpResponse('<h1>In Honda Racing Bike is CBR</h1>')

def hero(request):
    return HttpResponse('<h1> I hero Company Most selling bike is Glamer</h1>')
