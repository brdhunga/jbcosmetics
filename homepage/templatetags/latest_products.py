from django import template
from cartridge.shop.models import Product

register = template.Library()


@register.simple_tag
def get_latest():
    print("**"*30)
    print(dir(Product.objects.all()[0]))
    print("**"*30)
    products = Product.objects.all()
    return [e for e in products]

