from django.db import models
from core.models import BaseModel
from core.validators import html_file_validator, css_file_validator, validate_file_size
from sites.models import Site


class Footer(BaseModel):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name="footer")

    html_file = models.FileField(
        upload_to="footers/html/",
        validators=[html_file_validator, validate_file_size],
    )
    css_file = models.FileField(
        upload_to="footers/css/",
        validators=[css_file_validator, validate_file_size],
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Footer - {self.site.name}"
