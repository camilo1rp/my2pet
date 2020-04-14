from django.contrib.auth.models import User
from rest_framework import serializers

from categories.models import Category
from products.models import Product
from providers.models import Provider


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user"""

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for client"""

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category"""

    class Meta:
        model = Category
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product"""

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    provider = serializers.PrimaryKeyRelatedField(
        queryset=Provider.objects.all()
    )

    class Meta:
        model = Product
        fields = ('name', 'price', 'reference', 'category', 'provider', 'description')


class ProviderSerializer(serializers.ModelSerializer):
    """Serializer for providers"""

    class Meta:
        model = Provider
        fields = ('company', 'phone', 'email', 'address', 'userProvider', 'phoneProvider', 'emailProvider')
