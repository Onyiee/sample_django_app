from django.contrib import admin
from django.urls import path, include
from .views import display_image, more_images

urlpatterns = [
    path('', display_image, name="sample"),
    path('home', more_images, name="sample2")
]
