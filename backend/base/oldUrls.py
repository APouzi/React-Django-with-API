# from django.urls import path
# # Because they sit in the same folder, we can just do "."
# from . import views
# # from rest_framework_simplejwt.views import (TokenObtainPairView) #This is inherited from "from . import views" it has this same exact import.


# urlpatterns = [
#     path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
#     path('users/register/', views.registerUser, name = 'register' ),
    
#     path('users/profile/', views.getUserProfile, name ='users-profile'),
#     path('users/', views.getUsers, name ='users'),
#     path('products/', views.getProducts, name ='products'),
#     path('products/<str:pk>/', views.getProduct, name ='product'),
    
# ]