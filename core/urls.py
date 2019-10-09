from django.urls import path
from .views import home, offer, prices, about, order, contact

urlpatterns = [
    path('aktualnosci/', home, name='home'),
    path('oferta/', offer, name='offer'),
    path('cennik/', prices, name='prices'),
    path('o-nas/', about, name='about'),
    path('kontakt/', contact, name='contact')
]
