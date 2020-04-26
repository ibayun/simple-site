from django.contrib.auth.models import AbstractUser
from django.core.signing import TimestampSigner


class User(AbstractUser):
    signer = TimestampSigner(salt='Hello')

