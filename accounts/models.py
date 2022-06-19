from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Default user model. Extends AbstractUser
    """
    pass


