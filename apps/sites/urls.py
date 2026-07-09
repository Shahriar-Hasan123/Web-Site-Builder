from rest_framework_nested import routers
from django.urls import path, include

from .views import SiteViewSet
from pages.views import PageViewSet
from sections.views import SectionViewSet
from headers.views import HeaderDetailView
from footers.views import FooterDetailView

# /sites/
router = routers.DefaultRouter()
router.register(r"sites", SiteViewSet, basename="site")

# /sites/{site_pk}/pages/ 
sites_router = routers.NestedDefaultRouter(router, r"sites", lookup="site")
sites_router.register(r"pages", PageViewSet, basename="site-pages")

# /sites/{site_pk}/pages/{page_pk}/sections/
pages_router = routers.NestedDefaultRouter(sites_router, r"pages", lookup="page")
pages_router.register(r"sections", SectionViewSet, basename="page-sections")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(sites_router.urls)),
    path("", include(pages_router.urls)),

    path("sites/<int:site_pk>/header/", HeaderDetailView.as_view(), name="site-header"),
    path("sites/<int:site_pk>/footer/", FooterDetailView.as_view(), name="site-footer"),
]