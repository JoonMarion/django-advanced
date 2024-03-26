from django.contrib import admin
from .models import Product, Client


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
