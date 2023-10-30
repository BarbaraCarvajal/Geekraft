from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView #Para refrescar el token

urlpatterns = [
  path('register', views.register),
  path('login', views.LoginView.as_view()),
  path('refresh', TokenRefreshView.as_view()),
]

