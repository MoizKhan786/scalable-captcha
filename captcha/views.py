from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CaptchaImage
from .serializers import CaptchaImageSerializer
import random

class CaptchaImageViewSet(viewsets.ModelViewSet):
    queryset = CaptchaImage.objects.all()
    serializer_class = CaptchaImageSerializer

    @action(detail=False, methods=['get'])
    def random(self, request):
        captcha = random.choice(self.queryset)
        serializer = self.get_serializer(captcha)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def verify(self, request):
        instance = self.get_object()
        
        user_input_key = request.data.get('user_input_key')
        
        is_valid = instance.check_captcha_valid(user_input_key)
        return Response(dict(success=is_valid, message=""))