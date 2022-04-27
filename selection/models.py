from django.db import models


class Offer(models.Model):
    """Сущность ипотечное предложение"""
    bank = models.CharField("Название банка", max_length=50)
    term_min = models.IntegerField("Минимум лет выплат")
    term_max = models.IntegerField("Максимум лет выплат")
    rate_min = models.FloatField("Минимальный процент выплат")
    rate_max = models.FloatField("Максимальный процент выплат")
    payment_min = models.PositiveBigIntegerField("Сумма от")
    payment_max = models.PositiveBigIntegerField("Сумма до")

    @property
    def payment(self, price: int = None, deposit: float = None, term: int = None) -> float:
        if not price or deposit == None or not term:
            return 0
        else:
            P = self.rate_min / 12
            m = term * 12
            result = ((price * (1 - deposit / 100)) * P) / (1 - (1 + P) * (1 - m))
            return round(result, 2)

    class Meta:
        verbose_name = "Ипотека"
        verbose_name_plural = "Ипотеки"
