# profiles/urls.py
from django.urls import path
from .views import ProfileAPI

urlpatterns = [
    path('profile/<slug:slug>/', ProfileAPI.as_view(), name='profile-api'),
    path('profile/', ProfileAPI.as_view(), name='create-profile-api'),
]

