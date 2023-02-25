from django.contrib import admin
from .models import CarsFilms, CarsPersonages,CarsSamenvating,muziek,muziekAfbeelding,games

# Register your models here.
admin.site.register(CarsFilms)
admin.site.register(CarsPersonages)
admin.site.register(CarsSamenvating)
admin.site.register(muziek)
admin.site.register(muziekAfbeelding)
admin.site.register(games)