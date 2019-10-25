from django.shortcuts import render, redirect
from .models import Post
from .forms import ZamownienieForm, EmailForm
from django.contrib import messages
from django.core.mail import send_mail
from smtplib import SMTPException
from grave_web import settings
EMAIL = 'grave.legionowo@gmail.com'

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.order_by('-data')[:5]
    }
    print(context['posts'])
    return render(request,'core/home.html', context=context)

def offer(request):
    return render(request, 'core/offer.html')

def prices(request):
    return render(request, 'core/prices.html')

def order(request):
    if request.method == 'POST':
        form = ZamownienieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dziękujemy za złożenie zamówienia. Oczekuj emaila z potwierdzeniem.')
            return redirect('home')
    else:
        form = ZamownienieForm()
    return render(request, 'core/order.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            imie = form.cleaned_data['imie']
            nazwisko = form.cleaned_data['nazwisko']
            telefon = form.cleaned_data['telefon']
            user_subject = form.cleaned_data['tytuł']
            subject = f'[{imie} {nazwisko} - {telefon}] {user_subject}'
            user_message = form.cleaned_data['treść']
            message = f'{user_message}\n\nimie: {imie}\nnazwisko: {nazwisko}\ntelefon: {telefon}\nemail: {email}'
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [EMAIL])
                messages.success(request, 'Pomyślnie wysłano wiadomość.')
                redirect('contact')
            except SMTPException:
                messages.warning(request, 'Wystąpił błąd podczas wysyłania wiadomości. Spróbuj jeszcze raz.')
                redirect('contact')
    else:
        form = EmailForm()
    return render(request, 'core/contact.html', {'form': form})

def about(request):
    return render(request, 'core/about.html')