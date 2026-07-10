from django.db import models
from core.models import BaseModel
from core.validators import html_file_validator, css_file_validator, validate_file_size
from pages.models import Page


BLOCK_TYPE_CHOICES = [
    ("hero", "Hero Banner"),
    ("text", "Text Block"),
    ("gallery", "Image Gallery"),
    ("pricing_table", "Pricing Table"),
    ("contact_form", "Contact Form"),
]


class Section(BaseModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="sections")
    block_type = models.CharField(max_length=30, choices=BLOCK_TYPE_CHOICES)
    html_file = models.FileField(
        upload_to="sections/html/",
        validators=[html_file_validator, validate_file_size],
    )
    css_file = models.FileField(
        upload_to="sections/css/",
        validators=[css_file_validator, validate_file_size],
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.page.title} - {self.get_block_type_display()} (#{self.order})"
