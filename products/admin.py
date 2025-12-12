from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name","price","rating","size","image_url")
    search_fields = ("name","description")
    list_filter = ("size","rating")