from django.urls import path
from .views import ShortURLAPIView

urlpatterns = [
    path("", ShortURLAPIView.as_view(), name="shorturl_list"),
]
