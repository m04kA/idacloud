from django.urls import path, include

from . import views
from selection.views import OfferViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'offer', OfferViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


