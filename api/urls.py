from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.download_video, name='download_video')
]