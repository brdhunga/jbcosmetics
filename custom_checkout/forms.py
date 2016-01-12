from django import forms 

from cartridge.shop.models import Cart, CartItem, Order, DiscountCode
from cartridge.shop.forms import OrderForm


class CustomCheckoutForm(OrderForm):
    pass 


class CustomBillingShippingForm(OrderForm):
    class Meta:
        model = Order
        exclude = ("billing_detail_postcode", "billing_detail_country", "billing_detail_state",
                    "shipping_detail_postcode", "shipping_detail_country", "shipping_detail_state",)

