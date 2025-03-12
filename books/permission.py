
from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):

    def has_permission(self, request, view):
        return request.user 
    # and request.user.is_authenticated 
    # and request.user.is_librarian

class IsMember(BasePermission):

    def has_permission(self, request, view):
        return request.user 
    # and request.user.is_authenticated
    # and request.user.is_member
    
    