
from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    path('category/<str:categoryName>', views.productsByCategory, name='productsByCategory'),
    path('product/<int:id>/', views.productDetail, name='productDetail'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
]
