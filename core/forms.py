from django import forms
from .models import Zamowienie
from django.core.validators import RegexValidator
import datetime

class ZamownienieForm(forms.ModelForm):
    
    class Meta:
        model = Zamowienie
        exclude = ['data']
        widgets = {
            'data_usługi': forms.SelectDateWidget(),
            'data_urodzenia': forms.SelectDateWidget(years=range(1930, datetime.datetime.now().year+1)),
            'data_śmierci': forms.SelectDateWidget(years=range(1930, datetime.datetime.now().year+1)),
            'komentarz': forms.Textarea()
        }

class EmailForm(forms.Form):
    imie = forms.CharField(max_length=100)
    nazwisko = forms.CharField(max_length=100)
    telefon = forms.CharField(max_length=9, validators=[RegexValidator(r'^[0-9]{9}$','Numer musi zawierac 9 cyfr')])
    email = forms.EmailField()
    tytuł = forms.CharField(max_length=200)
    treść = forms.CharField(widget=forms.Textarea)