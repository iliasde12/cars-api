from django import forms
from django.forms import ModelForm
from .models import reviewsFilms



class ReviewForm(ModelForm):
   
    class Meta:
        model  = reviewsFilms
        fields = ('CarsFilm','naam','email','review')
        
        widgets= {
            'CarsFilm':forms.Select(attrs={'class':'form-control'}),
            'naam': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'review':forms.Textarea(attrs={'class':'form-control'}),
         }