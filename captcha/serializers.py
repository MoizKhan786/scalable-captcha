from rest_framework import serializers
from .models import CaptchaImage

class CaptchaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptchaImage
        fields = '__all__'