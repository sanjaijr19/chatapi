from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions

# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS
#
#
# class OwnerOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#
#         return request.user == obj.sender


class IsPostOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj.sender == request.user