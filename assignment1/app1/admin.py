from django.contrib import admin
from .models import User,Product,Order

# Register your models here.

class U(admin.ModelAdmin):
    list_filter = ['name']


class P(admin.ModelAdmin):
    list_display = ['name','price']
    list_filter = ['name']

class O(admin.ModelAdmin):
    list_display = ['quantity','user']
admin.site.register(User)
admin.site.register(Product,P)
admin.site.register(Order,O)
