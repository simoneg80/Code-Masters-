from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guide, Order
from .forms import OrderForm
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
    return render(request, 'home.html')

# Path for About Page
def about(request):
    return render(request, 'about.html')

# Path for Shop All Gudies Page
def guides_index(request):
    guides = Guide.objects.all()
    return render(request, 'guides/index.html', {'guides': guides})

# detail page
def guides_detail(request, guide_id):
    guide = Guide.objects.get(id = guide_id)
    return render(request, 'guides/detail.html', {
        'guide': guide
    })