import logging

from django.db import IntegrityError

from selection.models import Offer
from selection.serializers import OfferSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

logger = logging.getLogger("offer")


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
