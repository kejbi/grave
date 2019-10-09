from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# Models' names are in Polish, because of admin panel, which will be used by Pole

USLUGI = [
    ('og', 'Odwiedziny grobu'),
    ('sg', 'Sprzątanie grobu'),
    ('mn', 'Mycie nagrobka')
]

RODZAJE_GROBOW = [
    ('poj', 'Pojedyńczy'),
    ('pdw', 'Podwójny'),
    ('grb', 'Grobowiec')
]

CZESTOTLIWOSCI = [
    ('1', 'Raz w roku'),
    ('3', 'Trzy razy w roku'),
    ('6', 'Sześć razy w roku')
    ('12', 'Dwanaście razy w roku')
]

class Post(models.Model):
    tytul = models.CharField(max_length=200, null=False, blank=False)
    tresc = models.TextField(null=False, blank=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        print(f'{self.tytul} - {self.data}')

class Zamowienie(models.Model):
    imie = models.CharField(max_length=200, null=False, blank=False)
    nazwisko = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField()
    telefon = models.CharField(max_length=9, validators=[RegexValidator(r'^[0-9]{9}$','Numer musi zawierac 9 cyfr')])
    usluga = models.CharField(choices=USLUGI)
    rodzaj_grobu = models.CharField(choices=RODZAJE_GROBOW)
    czestotliwosc = models.CharField(choices=CZESTOTLIWOSCI)
    komentarz = models.TextField()