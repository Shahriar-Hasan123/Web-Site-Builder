from core.models import BaseModel
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Site(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sites")
    name = models.CharField(max_length=40)
    subdomain = models.SlugField(unique=True, blank=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.subdomain:
            self.subdomain = self._generate_unique_subdomain()
        super().save(*args, **kwargs)

    def _generate_unique_subdomain(self):
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 1
        while Site.objects.filter(subdomain=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        return self.name
