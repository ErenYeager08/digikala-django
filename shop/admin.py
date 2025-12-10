from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Customer)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'star', 'is_sale', 'sale_price', 'is_available', 'picture', 'descriptions']

admin.site.register(Order)