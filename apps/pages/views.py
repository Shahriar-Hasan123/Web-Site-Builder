from django.shortcuts import render
from .models import Page
from .serializers import PageSerializer, PageDetailSerializer
from rest_framework import viewsets, permissions

class PageViewSet(viewsets.ModelViewSet):
    """
    URL: /api/sites/{site_pk}/pages/
    """    
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Page.objects.filter(site_id=self.kwargs["site_pk"], site__owner=self.request.user)
    
    def get_serializer_class(self):
        if self.action=="retrieve":
            return PageDetailSerializer
        return PageSerializer
    
    def perform_create(self, serializer):
        serializer.save(site_id=self.kwargs["site_pk"])