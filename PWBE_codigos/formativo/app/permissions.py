from rest_framework.permissions import BasePermission

class IsGestor(BasePermission):
    message = "lalaalala"
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo =='G'
    
class IsProfessor (BasePermission):
    # permissão para acessar um método (view...)
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'P'
    
class IsDonoOuGestor(BasePermission):
    # permissão para consultar um objeto específico
    def has_object_permission(self, request, view, obj):
        if request.user.tipo == 'G':
            return True
        return obj.professor == request.user