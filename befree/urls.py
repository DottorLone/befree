# freebackend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('befreedemo.urls')),  # Includi gli URL della tua app qui
]
