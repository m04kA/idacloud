from rest_framework import serializers
from selection.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    """Сериалайзер для банковских предложений (CRUD)"""

    class Meta:
        model = Offer
        exclude = ("payment",)

    def validate(self, data):
        if data["term_min"] > data["term_max"]:
            raise serializers.ValidationError("Min years is more max years. It is wrong.")
        if data["term_min"] < 0:
            raise serializers.ValidationError("Years must be more 0!")
        if data["rate_min"] > data["rate_max"]:
            raise serializers.ValidationError("Min rate should be more max rate.")
        if data["rate_min"] < 0:
            raise serializers.ValidationError("Rate must be more 0!")
        if data["payment_min"] > data["payment_max"]:
            raise serializers.ValidationError("Min payment should be more max payment.")
        if data["payment_min"] < 0:
            raise serializers.ValidationError("Payment must be more 0!")
        return data


class OfferFilterSerializer(serializers.ModelSerializer):
    """Для фильтрации предложений"""
    class Meta:
        model = Offer
        fields = "__all__"

    def validate(self, data):
        if data["term_min"] > data["term_max"]:
            raise serializers.ValidationError("Min years is more max years. It is wrong.")
        if data["term_min"] < 0:
            raise serializers.ValidationError("Years must be more 0!")
        if data["rate_min"] > data["rate_max"]:
            raise serializers.ValidationError("Min rate should be more max rate.")
        if data["rate_min"] < 0:
            raise serializers.ValidationError("Rate must be more 0!")
        if data["payment_min"] > data["payment_max"]:
            raise serializers.ValidationError("Min payment should be more max payment.")
        if data["payment_min"] < 0:
            raise serializers.ValidationError("Payment must be more 0!")
        return data
