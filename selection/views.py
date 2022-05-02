from django.db.models import Q

from selection.models import Offer, payment_calculate
from selection.serializers import OfferSerializer, OfferFilterSerializer

from rest_framework import viewsets, filters



class OfferViewSet(viewsets.ModelViewSet):
    """CRUD for offer"""
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rate_min', 'payment']
    ordering = ['rate_min']

    def get_queryset(self):
        offers = Offer.objects.all()
        self.serializer_class = OfferSerializer
        price = self.request.query_params.get('price')
        deposit = self.request.query_params.get('deposit')
        term = self.request.query_params.get('term')
        if price is not None and deposit is not None and term is not None:
            try:
                price = int(price)
                deposit = float(deposit)
                term = int(term)
            except ValueError:
                return []
            offers = Offer.objects.filter(
                Q(payment_min__lte=price) & Q(payment_max__gte=price) &
                Q(term_min__lte=term) & Q(term_max__gte=term)
            )
            for el in offers:
                el.payment = payment_calculate(el, price=price, deposit=deposit, term=term)
                el.save()
            self.serializer_class = OfferFilterSerializer
        return offers
