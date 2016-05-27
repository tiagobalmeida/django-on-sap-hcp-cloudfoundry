from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def hello(request):
  return HttpResponse("Hello from django!")
