from rest_framework import permissions

class PermissionsClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
     
        if request.user.id == 1:
            return True
      
        if request.method == 'DELETE' and request.user.id != 1:
            return False
        print(request.method)
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user == obj.LightSample:
            return True