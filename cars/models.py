from operator import truediv
from django.db import models




# Create your models here.
class CarsFilms(models.Model):
    CarsFilm_Naam = models.CharField(max_length=200)
    CarsIntro = models.TextField(null=True)
    CarsTrailer = models.FileField(upload_to='static/Trailer/')
    CarsFilm_Afbeelding = models.FileField(upload_to='static/film/Afbeelding/' , null=True)
    CarsDescription = models.TextField()

    def __str__(self):
        return self.CarsFilm_Naam
    

class CarsPersonages(models.Model):
    carsfilm = models.ForeignKey(CarsFilms, on_delete=models.CASCADE ,null=True)
    CarsPersonage_Naam =  models.CharField(max_length=200 ,null=True)
    CarsPersonnage_Afbeelding = models.FileField(upload_to='static/personnage/Afbeelding/',null=True)
    CarsPersonageIntro = models.TextField(null = True)
    CarsPersonageDescription  = models.TextField(null=True)
    linksCarsSite1 = models.CharField(max_length = 700 , null=True)
    linksCarsSite2 = models.CharField(max_length = 700 , null=True)

    def __str__(self):
        return self.CarsPersonage_Naam 

class CarsSamenvating(models.Model):
    CarsFilm = models.ForeignKey(CarsFilms, on_delete=models.CASCADE ,null=True)
    SamenvattingTitle = models.CharField(max_length=200 ,null=True)
    SamenvatingDescriptie = models.TextField(null=True)

    def __str__(self) :
        return self.SamenvattingTitle


class muziek(models.Model):
    CarsFilm = models.ForeignKey(CarsFilms, on_delete=models.CASCADE ,null=True)
    MuziekNaam = models.CharField(max_length=200 ,null=True)
    artist = models.CharField(max_length=200 ,null=True)
    album = models.CharField(max_length=200 ,null=True)
    MuziekAfbeelding = models.FileField(upload_to='static/muziek/afbeelding/',null=True)
    MuziekBestand = models.FileField(upload_to='static/muziek/muziek/',null=True)

    def __str__(self) :
        return str(self.album)

class muziekAfbeelding(models.Model):
    CarsFilm = models.ForeignKey(CarsFilms, on_delete=models.CASCADE ,null=True)
    AlbumNaam = models.CharField(max_length=200 ,null=True)
    CarsAfbeeldingAlbum =  models.FileField(upload_to='static/muziek/afbeelding/cover/',null=True) 

    def __str__(self) :
        return str(self.AlbumNaam)
        

class games(models.Model):
    CarsFilm = models.ForeignKey(CarsFilms, on_delete=models.CASCADE ,null=True)
    GameNaam = models.CharField(max_length=200 ,null=True)
    gameAfbeelding = models.FileField(upload_to='static/games/afbeelding/',null=True)
    gameBeschrijving = models.TextField(null=True)

    def __str__(self):
        return str(self.id)