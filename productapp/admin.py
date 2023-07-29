from django.contrib import admin
from productapp.models import Category,Product,CartItem,Order,MyWishList,Coupen

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(MyWishList)
admin.site.register(Coupen)