from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    message = 'Измененять или удалять запись может только автор записи.'

    def has_object_permission(self, request, view, obj):

        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
