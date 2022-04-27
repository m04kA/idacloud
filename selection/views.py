from selection.models import Offer, Bank
from selection.serializers import OfferSerializer, BankSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class BankCreateView(APIView):
    def post(self, request):
        try:
            bank = BankSerializer(data=request.data)
            if bank.is_valid(raise_exception=True):
                bank.save()
                return Response(bank.data, status=201)
            return Response({"error": "Bad request"}, status=400)
        except:
            return Response({"error": "Bad request"}, status=400)


class BankListView(APIView):
    def get(self, response):
        banks = Bank.objects.all()
        banks = BankSerializer(banks, many=True).data
        return Response(banks, status=200)
