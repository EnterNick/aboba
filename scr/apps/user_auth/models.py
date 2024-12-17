from django.contrib.auth.models import AbstractUser
from django.db import models


def path_to_img(user, filename):
    return f'user_{user.id}/{filename}'


class CustomUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    avatar = models.ImageField(
        verbose_name='Аватар',
        default='profile.png',
        upload_to=path_to_img,
    )

    REQUIRED_FIELDS = [
        'email',
        'password',
        'first_name',
    ]

    is_seller = models.BooleanField(default=False)
