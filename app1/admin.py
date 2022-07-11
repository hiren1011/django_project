
from django.contrib import admin

from .models import Product, Signup
# Register your models here.

from django import template
register = template.Library()


@register.inclusion_tag('base1.html')



class products(admin.ModelAdmin):
    list_display=['name','price','des','image','review']
admin.site.register(Product,products)
admin.site.register(Signup)