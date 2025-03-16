from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('homepage/', views.homepage, name='homepage'),
    path('display_date/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
]

