from rest_framework import serializers
from shortener.models import ShortURL


class ShortURLGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ("original_url", "short_url", "times_followed", "created_at")

class ShortURLPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ["original_url"]

# class ShortURLReadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShortURL
#         fields = ["original_url", "times_followed", "created_at"]
#
# class ShortURLWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShortURL
#         fields = ["original_url"]