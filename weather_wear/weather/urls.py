from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import AboutView, GuestView
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),  #the path for our index view
    path('home/', TemplateView.as_view(template_name='home.html'), name="home"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', AboutView.as_view(), name="About"),
    path('guest/', GuestView.as_view(), name="guest"),
    path('accounts/', include('django.contrib.auth.urls')),

]
