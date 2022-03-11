# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework import serializers
# from rest_framework import response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import Response
# from .models import Product
# from django.contrib.auth.models import User

# from .products import products
# from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# from django.contrib.auth.hashers import make_password
# from rest_framework import status



# @apiview is from REST-Django framework, it's for function based views as we have here. 
# We can have POST, GET, DELETE, PUT
# @api_view(['GET'])
# def getRoutes(request):

#     routes = [
        
#         '/api/products/',
#         '/api/products/create/',

#         '/api/products/upload/',
#         '/api/products/<id>/reviews/',

#         '/api/products/top/',
#         '/api/products/<id>/',

#         '/api/products/delete/<id>/',
#         '/api/products/<update>/<id>/',

#     ]
#     return Response(routes, safe = False)

 





    