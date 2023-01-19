from django.contrib import admin

from django.contrib import admin
from mainapp.models import (
    Cart,
    CartProduct,
    Product,
    Category,
    Order,
    Customer
)

admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)