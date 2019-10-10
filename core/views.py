from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.order_by('-data')[:5]
    }
    print(context['posts'])
    return render(request,'core/home.html', context=context)

def offer(request):
    pass

def prices(request):
    pass

def order(request):
    pass

def contact(request):
    pass

def about(request):
    return render(request, 'core/about.html')