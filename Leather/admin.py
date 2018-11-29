from django.contrib import admin
from .models import *
from .models import Category,Product,Business,User_profile,Profile,Town,Post,Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Business)
admin.site.register(User_profile)
admin.site.register(Profile)
admin.site.register(Town)
admin.site.register(Post)
admin.site.register(Comment)
