from rest_framework import viewsets, permissions
from .models import Section
from .serializers import SectionSerializer


class SectionViewSet(viewsets.ModelViewSet):
    """
    URL: /api/sites/{site_pk}/pages/{page_pk}/sections/
    """

    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Section.objects.filter(
            page_id=self.kwargs["page_pk"],
            page__site_id=self.kwargs["site_pk"],
            page__site__owner=self.request.user,
        )

    def perform_create(self, serializer):
        serializer.save(page_id=self.kwargs["page_pk"])
