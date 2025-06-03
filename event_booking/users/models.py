from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Можно добавить поле типа is_organizer = models.BooleanField(default=False)
    pass
