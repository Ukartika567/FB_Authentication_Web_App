from os import name
from django.urls import path
from .import views

urlpatterns=[

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.handleSignup, name='handleSignup'),
    path('signin/', views.handleSignin, name='handleSignin'),
    path('logout/', views.logout, name='logout'),
    path('reset/', views.reset, name='reset'),
    path('postReset/', views.postReset, name='postreset'),

]