from django.db import models
from core.models import BaseModel
from sites.models import Site

# Create your models here.

STATUS_CHOICES = [
    ("draft", "Draft"),
    ("published", "Published"),
]


class Page(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="pages")
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    is_homepage = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    seo_meta = models.JSONField(default=dict, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("site", "slug")
        ordering = ["order"]

    def __str__(self):
        return f"{self.site.name} - {self.title}"
