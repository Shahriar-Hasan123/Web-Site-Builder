from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from .models import Header
from .serializers import HeaderSerializer
from sites.models import Site


class HeaderDetailView(generics.RetrieveUpdateAPIView):
    """
    URL: /api/sites/{site_pk}/header/
    """
    serializer_class = HeaderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        site = Site.objects.filter(id=self.kwargs["site_pk"], owner=self.request.user).first()
        if not site:
            raise NotFound("Site not found")
        header, _ = Header.objects.get_or_create(site=site)
        return header