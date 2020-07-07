from django.urls import path, include
from rest_framework.response import Response

from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView

from apis import views

class DocsView(APIView):
    """
    RESTFul Documentation of my app
    """
    def get(self, request, *args, **kwargs):
        apidocs = {'products': request.build_absolute_uri('product/'),
                   'categories': request.build_absolute_uri('category/'),
                   'providers': request.build_absolute_uri('provider/'),
                   'user creation': request.build_absolute_uri('user_create/'),
                   }
        return Response(apidocs)



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
    path('', DocsView.as_view()),
    path('', include(router.urls)),
    path('user_create/', views.CreateUserView.as_view(), name='user-create')
]
