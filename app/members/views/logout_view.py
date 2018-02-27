from django.contrib.auth import logout, get_user_model
from django.shortcuts import redirect

User = get_user_model()

__all__ = (
    'logout_view',
)


def logout_view(request):
    logout(request)
    return redirect('index')
