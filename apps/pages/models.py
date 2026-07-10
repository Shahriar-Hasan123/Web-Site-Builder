from django.db import models
from django.utils.text import slugify
from core.models import BaseModel
from sites.models import Site
from core.validators import css_file_validator, validate_file_size

STATUS_CHOICES = [("draft", "Draft"), ("published", "Published")]


class Page(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="pages")
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    is_homepage = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    seo_meta = models.JSONField(default=dict, blank=True)
    order = models.PositiveIntegerField(default=0)

    custom_css = models.FileField(
        upload_to="pages/css/",
        validators=[css_file_validator, validate_file_size],
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = ("site", "slug")
        ordering = ["order"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        if self.seo_meta is None:
            self.seo_meta = {}
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while (
            Page.objects.filter(site=self.site, slug=slug).exclude(pk=self.pk).exists()
        ):
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        return f"{self.site.name} - {self.title}"
