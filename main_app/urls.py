from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # about page below

    path('about/', views.about, name='about'),

    # shop page below
    path('guides/', views.guides_index, name='index'),

    #Detail page
    path('guides/<int:cat_id>', views.guides_detail, name='detail'),

]