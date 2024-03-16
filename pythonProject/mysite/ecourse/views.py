from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse("Hello world")
#
# def indexH1(request):
#     return HttpResponse("<h1>FUCKING ENGLISH</h1>")

from rest_framework import viewsets, permissions
from .models import Course, Category
from .serializer import CategorySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
