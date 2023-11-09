from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path("home", views.test_method),
    # path("auth", views.test_auth),
    # path("home", views.test_method),
    # path("", include("home.urls")),
    path("home", views.HomeView.as_view()),
    path("authorized", views.AuthorizedView.as_view()),
    # path("", views.HomeView.as_view(), name="home"),
    # path("login", views.LoginInterfaceView.as_view(), name="login"),
    # path("logout", views.LogoutInterfaceView.as_view(), name="logout"),
    # path("signup", views.SignupView.as_view(), name="signup"),
]
