# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.models import User

def sardana_ji(request):
    return HttpResponse("<h1>Welcome to the gorilla Page!</h1>")