from django.shortcuts import render
from django.http import HttpResponse
from home.models import Boutique
from django.http import JsonResponse
import json


# Create your views here.

def  hello(request):
   
   return HttpResponse("You are welcome")

def boutique(request):
   
   #boutiques = Boutique.objects.all().values()
   boutiquenames= Boutique.objects.values_list('name')
   #dict = json.dumps(list(boutiques))
   dict = json.dumps(list(boutiquenames))
   print(dict)
   response = JsonResponse(dict, status=200,safe=False)
   
   return response