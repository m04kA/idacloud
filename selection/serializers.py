from rest_framework import serializers
from selection.models import Bank, Offer


class OfferSerializer(serializers.ModelSerializer):
    """Сериалайзер для банковских предложений"""

    bank = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Offer
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    """Сериалайзер для банковских предложений"""

    class Meta:
        model = Bank
        fields = "__all__"
