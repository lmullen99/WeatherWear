from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),  #the path for our index view
    path('accounts/', include('django.contrib.auth.urls')),
]
