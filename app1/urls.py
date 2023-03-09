from app1.views import *
from django.urls import path
app_name='somthing'
urlpatterns=[
    path('tvs/',tvs,name='tvs'),
    path('bajaj',bajaj,name='bajaj'),
]