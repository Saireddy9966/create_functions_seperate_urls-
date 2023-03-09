from app2.views import *
from django.urls import path
app_name='somthing'
urlpatterns=[
    path('honda/',honda,name='honda'),
    path('hero/',hero,name='hero'),
]