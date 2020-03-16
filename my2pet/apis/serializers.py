
from django.contrib.auth.models import User
from rest_framework import serializers

from products.models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'reference', 'price', 'available', 'discount', 'delivery', 'available') # category missing

