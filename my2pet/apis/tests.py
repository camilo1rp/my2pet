from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from apis.serializers import ProductsSerializer
from categories.models import Category

from products.models import Product

PRODUCT_URL = reverse('apis:product-list')


def detail_url(product_id):
    return reverse('apis:product-detail', args=[product_id])


class PublicProductApis(TestCase):
    """Test the public apis for Product"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='test',
                                                         email='test@testing.com',
                                                         password='passtest123', )
        self.client.force_authenticate(self.user)

    def test_retrieving_product_list(self):
        """Test that products are retrieved"""
        Product.objects.create(name='product1', code='A12', price=10.00, )
        Product.objects.create(name='product2', code='A22', price=20.00, )

        res = self.client.get(PRODUCT_URL)

        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_creating_product(self):
        """Test that products are created"""
        payload = {
            'name': 'prod1',
            'code': 'A12',
            'price': 10.00,
            'reference': 'REF',
            'description': 'DESCRIPTION'
        }
        res = self.client.post(PRODUCT_URL, payload)
        exists = Product.objects.filter(name='prod1', code='A12', price=10.00).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['message'], "producto ha sido creado")
        self.assertTrue(exists)

    def test_retrieving_product_detail(self):
        """Test that product detail are retrieved"""
        payload = {
            'name': 'product1',
            'code': 'A12',
            'price': 20.00,
            'reference': 'REF',
            'description': 'DESCRIPTION',
        }
        product = Product.objects.create(**payload)
        print(product.id)
        url = detail_url(product.id)
        res = self.client.get(url)

        serializer = ProductsSerializer(product)
        self.assertEqual(res.data, serializer.data)


