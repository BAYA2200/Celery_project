from django.contrib import admin
from django.urls import path

from myapp.views import send_email

urlpatterns = [
    path('', send_email),
]
