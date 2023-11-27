from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
    # about page below
    path('about/', views.about, name="about"),
    # shop paget below


]