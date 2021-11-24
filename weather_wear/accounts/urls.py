# accounts/urls.py
from django.urls import path
from django.views.generic.base import TemplateView
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]