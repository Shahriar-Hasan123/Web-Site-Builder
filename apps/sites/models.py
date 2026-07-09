from core.models import BaseModel
from django.db import models
from django.contrib.auth.models import User


class Site(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sites")
    name = models.CharField(max_length=40)
    subdomain = models.SlugField(unique=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
