from rest_framework import permissions

from main.models import CartItem


class IsOwner(permissions.BasePermission):
    """ Права доступа владельцев Корзины """

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, CartItem):
            return obj.cart.user == request.user
        return obj.user == request.user
