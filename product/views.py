from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from .models import Product
from review.models import Review
from review.forms import ReviewForm
from user.models import Client
from rest_framework import generics
from .serializers import ProductSerializer

def productsByCategory(request, categoryName):
    products = Product.objects.filter(category=categoryName)
    translated_category_name = _(categoryName)
    return render(request, 'productsByCategory.html', {'category': translated_category_name, 'products': products})

def productDetail(request, id):
    reviews = Review.objects.filter(productReviewed=Product.objects.get(id=id))
    product = get_object_or_404(Product, id=id)
    sent_review = None
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            sent_review = review_form.save(commit=False)
            sent_review.productReviewed = product
            sent_review.reviewingClient = Client.objects.get(user=request.user)
            sent_review.save()
    else:
        review_form = ReviewForm()
    
    return render(request, 'productDetail.html', {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'sent_review': sent_review,
        'review_message': _('Your review has been successfully submitted.') if sent_review else None
    })

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
