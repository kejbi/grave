from django.db import models
from django.utils import timezone
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
    ('6', 'Sześć razy w roku'),
    ('12', 'Dwanaście razy w roku')
]

class Post(models.Model):
    tytul = models.CharField(max_length=200, null=False, blank=False)
    tresc = models.TextField(null=False, blank=False)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.tytul} - {self.data}'

class Zamowienie(models.Model):
    imię = models.CharField(max_length=200, null=False, blank=False)
    nazwisko = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefon = models.CharField(max_length=9, validators=[RegexValidator(r'^[0-9]{9}$','Numer musi zawierac 9 cyfr')], 
        null=False, blank=False)
    usługa = models.CharField(choices=USLUGI, max_length=100, null=False, blank=False)
    rodzaj_grobu = models.CharField(choices=RODZAJE_GROBOW, max_length=100, null=False, blank=False)
    częstotliwość = models.CharField(choices=CZESTOTLIWOSCI, max_length=100, null=False, blank=False)
    imię_zmarłego = models.CharField(max_length=200, null=False, blank=False)
    nazwisko_zmarłego = models.CharField(max_length=200, null=False, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True)
    data_śmierci = models.DateField(null=True)
    kwatera = models.CharField(max_length=10, null=True, blank=True)
    rząd = models.CharField(max_length=10, null=True, blank=True)
    nr_grobu = models.CharField(max_length=10, null=True, blank=True)
    komentarz = models.TextField(null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)
    data_usługi = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.imię} {self.nazwisko} - {self.usługa} / {self.data.strftime("%Y-%m-%d %H:%M:%S")}'