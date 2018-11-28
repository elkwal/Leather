from django.contrib import admin
from .models import Category,Product,Business,User_profile
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Business)
admin.site.register(User_profile)
