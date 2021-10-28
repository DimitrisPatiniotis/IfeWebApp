from django.contrib import admin
from django.urls import path

from .views import analysisView

urlpatterns = [
    path('overview', analysisView, name='analysis'),
]
