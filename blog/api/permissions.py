from lib2to3.pytree import Base
from pickle import GET
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS, IsAdminUser


class AuthorModifyOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        print(request.user)
        print(obj.author)
        print(request.user == obj.author)

        return request.user == obj.author


class IsAdminUserForObject(IsAdminUser):

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)