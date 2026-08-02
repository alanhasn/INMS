from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def role_required(*roles):
    """
    Restrict a view to logged-in users whose CustomUser.role is one of `roles`.
    Usage: @role_required(CustomUser.Roles.ADMIN, CustomUser.Roles.MANAGER)
    """
    def decorator(view_func):
        @login_required(login_url="login")
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role not in roles:
                raise PermissionDenied(
                    "You do not have permission to access this page."
                )
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
