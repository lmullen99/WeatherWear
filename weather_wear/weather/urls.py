from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView, RedirectView
from .views import AboutView, SignUpView
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path('index/', views.index, name='index'),  #the path for our index view
    path('home/', TemplateView.as_view(template_name='home.html'), name="home"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', AboutView.as_view(), name="About"),
    path('delete/', views.delete, name ="delete"),
    path('', views.guest, name="guest"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete/index', views.index),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))
]
