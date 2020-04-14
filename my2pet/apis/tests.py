from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from apis.serializers import ProductSerializer, CategorySerializer, ProviderSerializer

from categories.models import Category
from products.models import Product
from providers.models import Provider

PRODUCT_URL = reverse('apis:product-list')
CATEGORY_URL = reverse('apis:category-list')
PROVIDER_URL = reverse('apis:provider-list')


def detail_url(product_id):
    return reverse('apis:product-detail', args=[product_id])


def detail_category_url(category_id):
    return reverse('apis:category-detail', args=[category_id])


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
        serializer = ProductSerializer(products, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_creating_product(self):
        """Test that products are created"""
        category = Category.objects.create(name='pets')
        payload = {
            'name': 'prod1',
            'price': 10.00,
            'category': category.id,
            'reference': 'REF',
            'description': 'DESCRIPTION'
        }
        res = self.client.post(PRODUCT_URL, payload)
        exists = Product.objects.filter(name='prod1',
                                        price=10.00,
                                        category=category, ).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['message'], "Producto ha sido creado")
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
        url = detail_url(product.id)
        res = self.client.get(url)

        serializer = ProductSerializer(product)
        self.assertEqual(res.data, serializer.data)

    # def test_retrieving_branch_products(self):
    #     """"""

    def test_retrieving_categories(self):
        """Test that categories are retrieved"""
        Category.objects.create(name='personal care')
        Category.objects.create(name='pets care')

        res = self.client.get(CATEGORY_URL)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_creating_category(self):
        """Test that category can be created"""
        payload = {'name': 'pets'}
        res = self.client.post(CATEGORY_URL, payload)

        exists = Category.objects.filter(name=payload['name']).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_retrieving_category_detail(self):
        """Test that name is retrieved for category"""
        category = Category.objects.create(name='pets')
        url = detail_category_url(category.id)
        res = self.client.get(url)

        serializer = CategorySerializer(category)
        self.assertEqual(res.data, serializer.data)

    def test_retrieving_providers(self):
        """Test retrieving a list of providers"""
        Provider.objects.create(company='company', phone=12345567)
        Provider.objects.create(company='company2', phone=7654321)

        res = self.client.get(PROVIDER_URL)

        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_creating_provider(self):
        """Test creating a new provider"""
        payload = {
            'company': 'new_company',
            'phone': 1234567,
        }
        res = self.client.post(PROVIDER_URL, payload)

        exists = Provider.objects.filter(company=payload['company'],
                                         phone=payload['phone']).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)
