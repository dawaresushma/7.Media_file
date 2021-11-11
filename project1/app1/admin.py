from django.contrib import admin
from .models import Instagram
# Register your models here.

class InstagramAdmin(admin.ModelAdmin):
    list_display = ['img','content']

admin.site.register(Instagram,InstagramAdmin)