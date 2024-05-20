from django.contrib import admin
from django.urls import path, include
from user_onboarding.views.user_view import UserCreateView

urlpatterns = [
    path('track-api/user/create', UserCreateView.as_view()),
]
