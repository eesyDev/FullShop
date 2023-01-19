from django.db import models
from django.db.models import Sum, Count


def recalc_cart(cart):
    cart_data = cart.products.aggregate(Sum('final_price'), Count('id'))
    if cart_data.get('final_price__sum'):
        cart.final_price = cart_data['final_price__sum']
    else:
        cart.final_price = 0
    cart.total_products = cart_data['id__count']
    cart.save()