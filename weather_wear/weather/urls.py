from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import AboutView, GuestView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index),  #the path for our index view
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', AboutView.as_view(), name = "About"),
    path('guest/', GuestView.as_view(), name = "Guest"),

]
