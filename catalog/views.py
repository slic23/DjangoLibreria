from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello():
    return HttpResponse("Hello, world")
