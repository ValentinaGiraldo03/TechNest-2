from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext as _
from product.models import Product
from .models import CartProduct
from user.models import Client
from django.contrib import messages

# Create your views here.
def view_cart(request):
    cart_items = CartProduct.objects.filter(client=Client.objects.get(user=request.user))
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shoppingCart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartProduct.objects.get_or_create(
        product=product,
        client=Client.objects.get(user=request.user)
    )
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, _('Product added to cart successfully!'))
    
    return redirect('shoppingCart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartProduct.objects.get(id=item_id)
    cart_item.delete()
    messages.success(request, _('Product removed from cart successfully!'))
    
    return redirect('shoppingCart:view_cart')
