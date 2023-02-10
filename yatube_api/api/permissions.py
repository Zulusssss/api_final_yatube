from rest_framework import permissions

from rest_framework.exceptions import PermissionDenied


class AuthorOrReadOnly(permissions.BasePermission):

    # __message = 'Данный метод запроса недоступен анонимным пользователям.'
    # __message_obj = 'Удалять и изменять пост может только его автор.'

    # def has_permission(self, request, view):
    #     if (request.method in permissions.SAFE_METHODS or request.user.is_authenticated):
    #         return True
    #     raise PermissionDenied(detail=self.__message)

    # def has_object_permission(self, request, view, obj):
    #     if (obj.author == request.user or request.method in permissions.SAFE_METHODS):
    #         return True
    #     raise PermissionDenied(detail=self.__message_obj)

    # def has_permission(self, request, view): 

    #     return (request.method in permissions.SAFE_METHODS 

    #             or request.user.is_authenticated) 

 

    # def has_object_permission(self, request, view, obj): 

    #     return (obj.author == request.user 

    #             or request.method 

    #             in permissions.SAFE_METHODS)


    def has_permission(self, request, view): 

        return (request.method in permissions.SAFE_METHODS 

                or request.user.is_authenticated) 

 

    def has_object_permission(self, request, view, obj): 

        return (obj.author == request.user 

                or request.method 

                in permissions.SAFE_METHODS)

    
