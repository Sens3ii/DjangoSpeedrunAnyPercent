from django.contrib import admin
from .models import Item, Image, Category, Review

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Image)
admin.site.register(Review)
