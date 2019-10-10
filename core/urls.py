from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('oferta/', views.offer, name='offer'),
    path('cennik/', views.prices, name='prices'),
    path('o-nas/', views.about, name='about'),
    path('kontakt/', views.contact, name='contact')
]
