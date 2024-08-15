
from flask import request

class BasePermission:

    def has_permission(self):
        return True
    
class IsAuthenticated(BasePermission):

    def has_permission(self, request):
        return bool(hasattr(request, "user"))