from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')





# Path for About Page
def about(request):
    return render(request, 'about.html')











# Path for Shop Page
def shops_index(request):
    return render(request, 'forms/index.html')