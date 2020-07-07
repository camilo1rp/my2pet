from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from apis.serializers import ProductSerializer, CategorySerializer, ProviderSerializer

from categories.models import Category
from products.models import Product
from providers.models import Provider

CREATE_USER_URL = reverse('apis:user-create')

PRODUCT_URL = reverse('apis:product-list')
CATEGORY_URL = reverse('apis:category-list')
PROVIDER_URL = reverse('apis:provider-list')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


def detail_url(product_id):
    return reverse('apis:product-detail', args=[product_id])


def detail_category_url(category_id):
    return reverse('apis:category-detail', args=[category_id])


def detail_provider_url(provider_id):
    return reverse('apis:provider-detail', args=[provider_id])


class PublicUserApiTests(TestCase):
    """Test the user API public"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@testing.com',
            'password': 'testpass',
            'name': 'Test name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test that creating existing user fails"""
        payload = {'email': 'test@testing.com', 'password': 'pass1234'}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password is longer than 5 characters"""
        payload = {'email': 'test@testing.com', 'password': 'pw', 'name': 'Test',}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()

        self.assertFalse(user_exists)


class PublicProductApis(TestCase):
    """Test the public apis for Product"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(name='test',
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
        category = Category.objects.create(title='pets')
        provider = Provider.objects.create(company='new_company', phone=234567, phoneProvider=123456, )
        payload = {
            'name': 'prod1',
            'price': 10.00,
            'category': category.id,
            'provider': provider.id,
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
        Category.objects.create(title='personal care')
        Category.objects.create(title='pets care')

        res = self.client.get(CATEGORY_URL)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_creating_category(self):
        """Test that category can be created"""
        payload = {'title': 'pets'}
        res = self.client.post(CATEGORY_URL, payload)

        exists = Category.objects.filter(title=payload['title']).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_retrieving_category_detail(self):
        """Test that name is retrieved for category"""
        category = Category.objects.create(title='pets')
        url = detail_category_url(category.id)
        res = self.client.get(url)

        serializer = CategorySerializer(category)
        self.assertEqual(res.data, serializer.data)

    def test_retrieving_providers(self):
        """Test retrieving a list of providers"""
        Provider.objects.create(company='company', phone=12345567, phoneProvider=122345)
        Provider.objects.create(company='company2', phone=7654321, phoneProvider=122345)

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
            'phoneProvider': 123456,
        }
        res = self.client.post(PROVIDER_URL, payload)

        exists = Provider.objects.filter(company=payload['company'],
                                         phone=payload['phone']).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_updating_provider(self):
        """Test provider is updated and message is returned"""
        provider = Provider.objects.create(company='company',
                                           phone=1234567,
                                           phoneProvider=1234567)
        payload = {
            'company': 'new_company',
            'phone': 7654321,
            'phoneProvider': 765431,
        }
        url = detail_provider_url(provider.id)
        res = self.client.put(url, payload)
        provider.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['message'], "Proveedor ha sido editado")
        self.assertEqual(provider.company, payload['company'])

    def test_deleting_provider(self):
        """Test that provider is deleted"""
        provider = Provider.objects.create(company='company',
                                           phone=1234567,
                                           phoneProvider=1234567)

        url = detail_provider_url(provider.id)
        res = self.client.delete(url)

        providers = Provider.objects.all()

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(providers), 0)
