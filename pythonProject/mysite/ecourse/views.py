from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def indexH1(request):
    return HttpResponse("<h1>FUCKING ENGLISH    </h1>")