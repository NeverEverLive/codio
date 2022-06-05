from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from blog.views import post_detail, post_list

urlpatterns = [
    path('posts/', post_list, name='api_post_list'),
    path('posts/<int:pk>', post_detail, name='api_post_detail'),
    path('auth/', include('rest_framework.urls')),
    path('token-auth/', obtain_auth_token)
]
