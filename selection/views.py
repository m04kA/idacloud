import logging

from django.db import IntegrityError

from selection.models import Offer
from selection.serializers import OfferSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger("offer")


class OffersListView(APIView):
    def get(self, response):
        offers = Offer.objects.all()
        offers = OfferSerializer(offers, many=True).data
        return Response(offers, status=200)


class OfferCreateView(APIView):

    def post(self, request):
        try:
            offer = OfferSerializer(data=request.data)
            if offer.is_valid(raise_exception=True):
                try:
                    offer.save()
                except IntegrityError as identifier:
                    return Response({
                        "message": str(identifier)
                    }, status=400)

                return Response(offer.data, status=201)
            return Response({"error": "Bad request"}, status=400)
        except Exception as ex:
            return Response({"error": ex}, status=400)


class OfferUpdateView(APIView):
    def patch(self, request, pk):
        # pk = kwargs.get('pk', None)
        if not pk:
            logger.error(f"Bad request for update offer. data: {request.data}")
            return Response({"error": "Method PUT is not allowed"}, status=400)
        try:
            logger.info(f"Get detail info about offer (id - {pk})")
            instance = Offer.objects.get(pk=pk)
        except Offer.DoesNotExist:
            logger.error(f"offer (id - {pk}) does not exists")
            return Response({"error": "Object does not exists"}, status=400)
        update_offer = OfferSerializer(instance, data=request.data, partial=True)
        update_offer.is_valid(raise_exception=True)
        update_offer.save()
        logger.info(f"Successful update offer (id - {pk})")
        return Response({"put": update_offer.data}, status=202)


class OfferDeleteView(APIView):
    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            logger.error(f"Bad request for DELETE offer.")
            return Response({"error": "Method DELETE is not allowed"}, status=400)
        try:
            logger.info(f"Get detail info about offer (id - {pk})")
            offer = Offer.objects.get(id=pk)
        except Offer.DoesNotExist:
            logger.error(f"Offer (id - {pk}) does not exists")
            return Response({"error": "Object does not exists"}, status=400)
        seriolazer = OfferSerializer(offer).data
        logger.info(f"Delete offer (id - {pk})")
        offer.delete()
        return Response(seriolazer, status=204)
