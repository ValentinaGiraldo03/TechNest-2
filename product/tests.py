from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Monitor LG",
            description="Monitor 24 pulgadas Full HD",
            price=300.0,
            brand="LG",
            category="Screen",
            stock=10
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Monitor LG")
        self.assertEqual(product.brand, "LG")
        self.assertEqual(product.price, 300.0)
        self.assertEqual(product.category, "Screen")
        self.assertEqual(product.stock, 10)


class ProductAPITest(APITestCase):
    def setUp(self):
        Product.objects.create(
            name="Mouse Logitech",
            description="Mouse inalámbrico",
            price=50.0,
            brand="Logitech",
            category="Mouse",
            stock=20
        )

    def test_get_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Mouse Logitech")
        self.assertEqual(response.data[0]['brand'], "Logitech")
