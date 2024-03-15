from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('indexH1/', views.indexH1, name="ham1"),
]