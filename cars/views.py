from multiprocessing import context
from unittest import loader
from urllib import request
from django.shortcuts import render
from .models import CarsFilms, CarsPersonages,CarsSamenvating, muziek,games
from rest_framework import generics
from .serializers import CarsFilmsSerializer,CarsPersonagesSerializer,CarsSamenvatingSerializer,muziekSerializer,gamesSerializer

# Create your views here.

#api
class CarsFilmsListCreateView(generics.ListCreateAPIView):
    queryset = CarsFilms.objects.all()
    serializer_class = CarsFilmsSerializer
    template_name = 'carsfilms_list.html'

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


class gamesList(generics.ListCreateAPIView):
    queryset = games.objects.all()
    serializer_class = gamesSerializer

class gamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = games.objects.all()
    serializer_class = gamesSerializer

def home(request):
  return render(request,"index.html")