from uuid import uuid4

from django.db import models


class AccessKey(models.Model):
    key = models.CharField(max_length=40, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)
