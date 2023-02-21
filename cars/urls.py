from unicodedata import name
from django.urls import path , re_path , reverse

from . import views

urlpatterns = [
   #api
    path('',views.home,name="index"),
    path('carsfilms/', views.CarsFilmsListCreateView.as_view(), name='carsfilms-list-create'),
    path('carsfilms/<int:pk>/', views.CarsFilmsDetail.as_view(), name='carsfilms-detail'),
    path('carspersonages/', views.CarsPersonagesList.as_view(), name='carspersonages-list'),
    path('carspersonages/<int:pk>/', views.CarsPersonagesDetail.as_view(), name='carspersonages-detail'),
    path('carssamenvating/', views.CarsSamenvatingList.as_view(), name='carssamenvating-list'),
    path('carssamenvating/<int:pk>/', views.CarsSamenvatingDetail.as_view(), name='carssamenvating-detail'),
    path('reviewsfilms/', views.reviewsFilmsList.as_view(), name='reviewsfilms-list'),
    path('reviewsfilms/<int:pk>/', views.reviewsFilmsDetail.as_view(), name='reviewsfilms-detail'),
    path('muziek/', views.muziekList.as_view(), name='muziek-list'),
    path('muziek/<int:pk>/', views.muziekDetail.as_view(), name='muziek-detail'),
    path('muziekafbeelding/', views.muziekAfbeeldingList.as_view(), name='muziekafbeelding-list'),
    path('muziekafbeelding/<int:pk>/', views.muziekAfbeeldingDetail.as_view(), name='muziekafbeelding-detail'),
    path('game/', views.gamesList.as_view(), name='game-list'),
    path('game/<int:pk>/', views.gamesDetail.as_view(), name='game-detail'),

   ]
   

