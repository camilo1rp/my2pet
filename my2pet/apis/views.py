from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserSerializer, ClientSerializer, ProductSerializer
from categories.models import Category


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        if request.method == 'GET':
            email = request.GET.get('email')
            password = request.GET.get('password')
            company = request.GET.get('company')
            cat_id = request.GET.get('category')
            serializer = UserSerializer(data={'username': company, 'email': email, 'password': password})
            if serializer.is_valid():
                us = serializer.save()
                try:
                    cat = Category.objects.get(id=cat_id)
                    us.profile.category = cat
                except:
                    return JsonResponse('***Category does not exist ****', safe=False)
                us.profile.company = company
                us.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse('***Error al Registrar ****', safe=False)


class ClientGetViewSet(viewsets.ModelViewSet):
    def list(self, request):
        print(' ----  list clients ---- ')
        users = User.objects.exclude(is_staff=True).order_by('-is_active', '-date_joined')
        value_data = []
        value1 = ["name", "apellido", "phone", "tipo identificacion", "numero identificacion",
                  "address", "email", "fecha de nacimiento", "editar", "estado"]
        for user in users:
            info = {}
            info['id'] = user.id
            info['firstName'] = user.first_name
            info['lastName'] = user.last_name
            info['phone'] = user.client.phone
            info['id_type'] = user.client.id_type
            info['id_number'] = user.client.id_number
            info['address'] = user.client.address
            info['email'] = user.email
            info['birth'] = user.client.dob
            info['active'] = user.is_active
            value_data.append(info)
        value = [value1, value_data]
        return JsonResponse(value, safe=False)


class ProductViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        if request.method == 'GET':
            print("****request client*****")
            product_id = request.GET.get('idProduct')
            name = request.GET.get('name')
            reference = request.GET.get('reference')
            price = request.GET.get('price')
            category = request.GET.get('category')
            available = request.GET.get('available')
            delivery = request.GET.get('delivery')
            discount = request.GET.get('discount')
            description = request.GET.get('description')

            if product_id:
                # user = User.objects.get(id=user_id)
                # if delete:
                #     user.is_active = not user.is_active
                #     user.save()
                #     return JsonResponse('Eliminado Exitosamente', safe=False)
                # user.first_name = first_name
                # user.last_name = last_name
                # user.client.dob = dob
                # user.client.email = email
                # user.client.phone = phone
                # user.client.address = address
                # user.client.id_type = id_type
                # user.client.id_number = id_number
                # user.client.save()
                # user.save()
                return JsonResponse('Actualizado Exitosamente', safe=False)
            else:
                serializer = ProductSerializer(data={'name': name, 'reference': reference,
                                                     'price': price, 'category': category,
                                                     'available': available, 'delivery': delivery,
                                                     'discount': discount, 'description': description,
                                                     })
                if serializer.is_valid():
                    prod = serializer.save()
                    print("product saved")
                    return JsonResponse('Producto Creado Exitosamente', safe=False)
                return JsonResponse('Error al Registrar', safe=False)
        return JsonResponse('Error al Registrar', safe=False)


class ClientViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        if request.method == 'GET':
            print("****request client*****")
            user_id = request.GET.get('idUser')
            first_name = request.GET.get('firstName')
            last_name = request.GET.get('lastName')
            dob = request.GET.get('birthDate')
            email = request.GET.get('email')
            phone = request.GET.get('phone')
            address = request.GET.get('address')
            id_type = request.GET.get('typeIndentification')
            id_number = request.GET.get('indentification')
            delete = request.GET.get('delete')
            if user_id:
                user = User.objects.get(id=user_id)
                if delete:
                    user.is_active = not user.is_active
                    user.save()
                    return JsonResponse('Eliminado Exitosamente', safe=False)
                user.first_name = first_name
                user.last_name = last_name
                user.client.dob = dob
                user.client.email = email
                user.client.phone = phone
                user.client.address = address
                user.client.id_type = id_type
                user.client.id_number = id_number
                user.client.save()
                user.save()
                return JsonResponse('Actualizado Exitosamente', safe=False)
            else:
                serializer = ClientSerializer(data={'username': first_name[:4] + last_name[:3], 'email': email,
                                                    'password': 'Abc1234', 'first_name': first_name,
                                                    'last_name': last_name})
                if serializer.is_valid():
                    us = serializer.save()
                    us.client.phone = phone
                    us.client.dob = dob
                    us.client.address = address
                    us.client.id_type = id_type
                    us.client.id_number = id_number
                    us.client.is_client = True
                    us.save()
                    return JsonResponse('Creado Exitosamente', safe=False)
                return JsonResponse('Error al Registrar', safe=False)
        return JsonResponse('Error al Registrar', safe=False)
