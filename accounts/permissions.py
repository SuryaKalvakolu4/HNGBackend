import jwt

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.conf import settings

from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken


class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        token = ""
        try:
            is_blackListed = BlacklistedToken.objects.get(token__token=token)
            if is_blackListed:
                is_allowed_user = False
        except BlacklistedToken.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user
