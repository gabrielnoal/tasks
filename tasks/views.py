from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get(request):
    return HttpResponse("GET")

def add(request):
    return HttpResponse("ADD")

def delete(request):
    return HttpResponse("DELETE")
