from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'librarian', False)

class IsMember(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'member', False)

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'admin', False)
    
    