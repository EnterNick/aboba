from django.contrib.auth.models import AnonymousUser


def get_user(request):
    return (
        request.user
        if request.user is not AnonymousUser
        and request.user.is_authenticated
        and request.COOKIES.get('accessToken') is not None
        else 'none'
    )
