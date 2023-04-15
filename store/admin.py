from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)
