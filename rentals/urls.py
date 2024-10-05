from django.urls import path
from .views import fetch_book_details

urlpatterns = [
    path('fetch-book/<str:title>/', fetch_book_details, name='fetch_book'),
]
