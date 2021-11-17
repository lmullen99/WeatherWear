from django.urls import path, include
from . import views
from .views import AboutView, GuestView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),  #the path for our index view
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', AboutView.as_view(), name = "About"),
    path('custom/', GuestView.as_view(), name = "Guest"),

]
