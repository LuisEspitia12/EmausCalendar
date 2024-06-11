from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('',views.home, name="home"),
]
