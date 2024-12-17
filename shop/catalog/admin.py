from django.contrib import admin
from .models import Category, Product

# Register your models here.
# Для работы с моделями в админ-панели


admin.site.register(Category)
admin.site.register(Product)
