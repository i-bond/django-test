from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from shortener.models import ShortURL
from .serializers import ShortURLGETSerializer, ShortURLPOSTSerializer
from shortener.utils import create_random_code

class ShortURLAPIView(generics.ListCreateAPIView): # GET all links
    queryset = ShortURL.objects.all()
    # serializer_class = ShortURLGETSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ShortURLGETSerializer

        return ShortURLPOSTSerializer

    def perform_create(self, serializer):
        short_url = create_random_code()
        if ShortURL.objects.filter(short_url=short_url).exists():
            short_url = create_random_code()
        serializer.save(short_url=short_url)








