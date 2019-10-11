from django.shortcuts import render, redirect
from .models import Post
from .forms import ZamownienieForm
from django.contrib import messages

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
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')