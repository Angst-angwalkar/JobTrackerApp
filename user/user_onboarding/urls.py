from django.contrib import admin
from django.urls import path, include
from user_onboarding.views.user_view import UserCreateView, UserView
from user_onboarding.views.auth_view import LoginView

urlpatterns = [
    path('track-api/user/create', UserCreateView.as_view()),
    path('track-api/login', LoginView.as_view()),
    path('track-api/user/', UserView.as_view()),
]
