from django.db import models
from core.models import BaseModel
from core.mixins import AuditModelMixin
from  django.contrib.auth.models import AbstractUser


class Account(BaseModel,
              AuditModelMixin,
              AbstractUser):

    first_name = models.CharField(
        max_length=64,
        default='',
        blank=True
    )
    last_name = models.CharField(
        max_length=64,
        default='',
        blank=True
    )

    # Meta class, other fields, methods, etc
