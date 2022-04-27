from rest_framework import serializers
from selection.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    """Сериалайзер для банковских предложений"""

    class Meta:
        model = Offer
        fields = "__all__"

    def create(self, validated_data):
        return Offer.objects.create(**validated_data)
