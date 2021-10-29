from django.contrib import admin
from django.urls import path

from .views import analysisView, homeView

urlpatterns = [
    path('', homeView, name='home'),
    path('overview/', analysisView, name='analysis'),
]
