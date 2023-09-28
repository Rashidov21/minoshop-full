from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_image','address', 'phone']
    
    def user_image(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" />')
