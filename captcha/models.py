import uuid
from django.db import models

class CaptchaImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
    image = models.ImageField(upload_to="captcha_images/")
    key_content = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{str(self.id)[:6]} | {self.key_content}" 
    
    def check_captcha_valid(self, user_input_key):
        return self.key_content == user_input_key
            