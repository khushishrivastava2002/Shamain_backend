from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from .models import *
# Create your views here.
def Musicandband(request):
   data=list(MusicandBand1.objects.values())
   return JsonResponse(data,safe=False)

def Movieandseries1(request):
   data1=list(Movieandseries.objects.values())
   return JsonResponse(data1,safe=False)

def Sports1(request):
   data2=list(sports.objects.values())
   return JsonResponse(data2,safe=False)

def Persona1(request):
   data3=list(sports.objects.values())
   return JsonResponse(data3,safe=False)

def Dripdoodle1(request):
   data4=list(sports.objects.values())
   return JsonResponse(data4,safe=False)

def Anime1(request):
   data5=list(sports.objects.values())
   return JsonResponse(data5,safe=False)

def Abstract1(request):
   data6=list(sports.objects.values())
   return JsonResponse(data6,safe=False)

def Comics1(request):
   data7=list(sports.objects.values())
   return JsonResponse(data7,safe=False)

def Sanskriti1(request):
   data8=list(sports.objects.values())
   return JsonResponse(data8,safe=False)