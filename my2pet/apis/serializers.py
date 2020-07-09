from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

from categories.models import Category
from products.models import Product
from providers.models import Provider


class UserSerializer(serializers.ModelSerializer):
    """Serializer for Users administrators"""

    class Meta:
        model = get_user_model()
        fields = ('name', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = "Credenciales no validas."
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for client"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category"""

    class Meta:
        model = Category
        fields = ('id', 'title')


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
        fields = ('id', 'name', 'price', 'reference', 'category', 'provider', 'description')


class ProviderSerializer(serializers.ModelSerializer):
    """Serializer for providers"""

    class Meta:
        model = Provider
        fields = ('id', 'company', 'phone', 'email',
                  'address', 'userProvider', 'phoneProvider',
                  'emailProvider', 'observations')
