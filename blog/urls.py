from django.urls import path, include

from blog.views import post_detail, post_list

urlpatterns = [
    path('posts/', post_list, name='api_post_list'),
    path('posts/<int:pk>', post_detail, name='api_post_detail'),
]