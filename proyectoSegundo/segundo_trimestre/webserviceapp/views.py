from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

# Create your views here.


def pagina_de_prueba(request):
    return HttpResponse("<h2>AAAAAAAAAAAAAAAAAA</h2>")
