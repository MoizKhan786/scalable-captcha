from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CaptchaImage

@admin.register(CaptchaImage)
class CaptchaImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'key_content', 'image_preview',)
    list_display_links = ('id', 'key_content',)
    readonly_fields = ('id', 'image_preview',)
    
    fieldsets = (
        ("Captcha Image Information", {
            'fields': ('id', 'key_content', 'image', 'image_preview',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 200px;" />')
        return None

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
