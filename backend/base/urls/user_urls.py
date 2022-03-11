from django.urls import path
# Because they sit in the same folder, we can just do "."
from base.views import user_views as views
# from rest_framework_simplejwt.views import (TokenObtainPairView) #This is inherited from "from . import views" it has this same exact import.


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),

    path('profile/', views.getUserProfile, name="users-profile"),
    path('profile/update/', views.updateUserProfile, name="users-profile-update"),
    path('', views.getUsers, name ='users'),

]