from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from blog.api.views import PostList, PostDetail, UserDetail

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(),
        name="api_post_detail"),
    path('users/<str:username>', UserDetail.as_view(),
        name='api_user_detail'),
    path('auth/', include('rest_framework.urls')),
    path('token-auth/', obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)