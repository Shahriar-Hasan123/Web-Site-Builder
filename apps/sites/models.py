from django.conf import settings
from django.db import models

from apps.core.models import BaseModel
from apps.core.validators import validate_file_size, css_file_validator


class Site(BaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        SUSPENDED = "suspended", "Suspended"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sites",
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    domain = models.CharField(max_length=255, blank=True, null=True, unique=True)
    is_domain_verified = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    favicon = models.ImageField(
        upload_to="sites/favicons/",
        validators=[validate_file_size],
        blank=True,
        null=True,
    )
    logo = models.ImageField(
        upload_to="sites/logos/",
        validators=[validate_file_size],
        blank=True,
        null=True,
    )
    global_css = models.FileField(
        upload_to="sites/css/",
        validators=[css_file_validator, validate_file_size],
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
