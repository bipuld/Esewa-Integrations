from django.contrib import admin
from . models import Product,ProductDetail
from django.utils.html import  format_html

# Register your models here.
admin.site.register(Product)

@admin.register(ProductDetail)
class Product(admin.ModelAdmin):
    def thumbnail(self,obj):
        return format_html('<img src="{}" width="40" style="border-radius :50px;"/>'.format(obj.images.url))
    thumbnail.short_description='product_image'
    list_display=['id','thumbnail','price','tax_price','service_charge','total_price']
    list_display_links=['id','total_price']
    