from django.contrib import admin
from .models import Link
# Register your models here.

class Link(admin.ModelAdmin):
    list_display = [
        'target_url', 'description', 'identifier', 'author', 'created_date', 'active'
    ]