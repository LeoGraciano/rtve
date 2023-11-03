from corsheaders.conf import conf
from rest_framework.permissions import (
    BasePermission,
    DjangoModelPermissionsOrAnonReadOnly,
)


class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.owner == request.user


class IsAllowedCORSOrigin(BasePermission):
    def has_permission(self, request, view):
        allowed_origins = conf.CORS_ALLOWED_ORIGINS
        print(allowed_origins)

        origin = request.headers.get("Origin")
        print(origin)
        return origin in allowed_origins


class AnyPermission(BasePermission):
    permissions = [
        DjangoModelPermissionsOrAnonReadOnly,
        IsAllowedCORSOrigin,
    ]

    def has_permission(self, request, view):
        for permission in self.permissions:
            if permission().has_permission(request, view):
                return True
        return False
