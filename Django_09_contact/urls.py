# from django.contrib import admin
from django.urls import path, include
from contact import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', include('contact.urls')),
]
