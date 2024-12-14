from django.urls import path
from .views import *
from .views import sardana_ji


urlpatterns = [
    path('cutiepie/', sardana_ji,name='cuteboy')
]