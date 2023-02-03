
from django.urls import path
# from .views import ShortURLStats
from .views import short_url_home, redirect_to_website

urlpatterns = [
    path("", short_url_home, name='stats'),
    path("<str:token>", redirect_to_website, name='redirect_to_website')
]







