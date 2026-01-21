from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_REQUESTER = 'REQUESTER'
    ROLE_RESOLVER = 'RESOLVER'
    ROLE_ADMIN = 'ADMIN'

    ROLE_CHOICES = [
        (ROLE_REQUESTER, 'Solicitante'),
        (ROLE_RESOLVER, 'Resolutor'),
        (ROLE_ADMIN, 'Administrador'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_REQUESTER
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
