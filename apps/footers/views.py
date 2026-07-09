from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from .models import Footer
from .serializers import FooterSerializer
from sites.models import Site


class FooterDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = FooterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        site = Site.objects.filter(
            id=self.kwargs["site_pk"], owner=self.request.user
        ).first()
        if not site:
            raise NotFound("Site not found")

        footer, _ = Footer.objects.get_or_create(site=site)
        return footer