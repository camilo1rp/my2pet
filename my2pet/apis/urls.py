from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apis import views

router = DefaultRouter()
# router.register(r'signUp', views.UserViewSet, basename='signUp')
# router.register(r'getClient', views.ClientGetViewSet, basename='getClient')
# router.register(r'addClient', views.ClientViewSet, basename='addClient')
# router.register(r'addProduct', views.ProductViewSet, basename='addProduct')
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('provider', views.ProviderViewSet)

app_name = 'apis'

urlpatterns = [
    path('', include(router.urls))
]
