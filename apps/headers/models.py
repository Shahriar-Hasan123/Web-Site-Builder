from django.db import models
from core.models import BaseModel
from core.validators import css_file_validator, html_file_validator, validate_file_size
from sites.models import Site

# Create your models here.


class Header(BaseModel):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name="header")
    html_file = models.FileField(
        upload_to="headers/html/",
        validators=[html_file_validator, validate_file_size],
    )
    css_file = models.FileField(
        upload_to="headers/css/",
        validators=[css_file_validator, validate_file_size],
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Header - {self.site.name}"
