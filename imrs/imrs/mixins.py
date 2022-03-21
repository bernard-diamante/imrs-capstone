from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class AdminAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an admin."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        elif not request.user.is_organisor:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)

class MainOfficeAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is a main office employee."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        elif not request.user.userRole == 1:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)

class WarehouseAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is a warehouse manager."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        elif not request.user.userRole == 2:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)

class SiteAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is a project site manager."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        elif not request.user.userRole == 3:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)