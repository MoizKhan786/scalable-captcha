from rest_framework.routers import DefaultRouter
from .views import CaptchaImageViewSet

router = DefaultRouter()
router.register(r'', CaptchaImageViewSet)