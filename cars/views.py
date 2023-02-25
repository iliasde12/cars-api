from multiprocessing import context
from re import template
from unittest import loader
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse , Http404, HttpResponseRedirect
from django.template import loader
from .models import CarsFilms, CarsPersonages,CarsSamenvating, muziek, muziekAfbeelding,games
from django.db.models import Q
from django.views.generic import TemplateView
from django.urls import reverse
from rest_framework import generics
from .serializers import CarsFilmsSerializer,CarsPersonagesSerializer,CarsSamenvatingSerializer,muziekSerializer,muziekAfbeeldingSerializer,gamesSerializer

# Create your views here.

#api
class CarsFilmsListCreateView(generics.ListCreateAPIView):
    queryset = CarsFilms.objects.all()
    serializer_class = CarsFilmsSerializer

class CarsFilmsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarsFilms.objects.all()
    serializer_class = CarsFilmsSerializer

class CarsPersonagesList(generics.ListCreateAPIView):
    queryset = CarsPersonages.objects.all()
    serializer_class = CarsPersonagesSerializer

class CarsPersonagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarsPersonages.objects.all()
    serializer_class = CarsPersonagesSerializer

class CarsSamenvatingList(generics.ListCreateAPIView):
    queryset = CarsSamenvating.objects.all()
    serializer_class = CarsSamenvatingSerializer

class CarsSamenvatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarsSamenvating.objects.all()
    serializer_class = CarsSamenvatingSerializer
    

class muziekList(generics.ListCreateAPIView):
    queryset = muziek.objects.all()
    serializer_class = muziekSerializer

class muziekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = muziek.objects.all()
    serializer_class = muziekSerializer

class muziekAfbeeldingList(generics.ListCreateAPIView):
    queryset = muziekAfbeelding.objects.all()
    serializer_class = muziekAfbeeldingSerializer

class muziekAfbeeldingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = muziekAfbeelding.objects.all()
    serializer_class = muziekAfbeeldingSerializer

class gamesList(generics.ListCreateAPIView):
    queryset = games.objects.all()
    serializer_class = gamesSerializer

class gamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = games.objects.all()
    serializer_class = gamesSerializer

def home(request):
  return render(request,"index.html")