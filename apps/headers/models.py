from django.db import models
from core.models import BaseModel
from sites.models import Site

# Create your models here.


class Header(BaseModel):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name="header")
    content=models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return f"Header - {self.site.name}"