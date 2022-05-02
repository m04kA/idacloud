from django.db import models


class Offer(models.Model):
    """The essence of the mortgage offer"""
    payment = models.FloatField("Ежемесячный платёж", default=0)
    bank = models.CharField("Название банка", max_length=50)
    term_min = models.IntegerField("Минимум лет выплат")
    term_max = models.IntegerField("Максимум лет выплат")
    rate_min = models.FloatField("Минимальный процент выплат")
    rate_max = models.FloatField("Максимальный процент выплат")
    payment_min = models.PositiveBigIntegerField("Сумма от")
    payment_max = models.PositiveBigIntegerField("Сумма до")

    class Meta:
        verbose_name = "Ипотека"
        verbose_name_plural = "Ипотеки"


def payment_calculate(self, price: int = None, deposit: float = None, term: int = None) -> float:
    """
    Function for calculating monthly payment
    :self: - object offer
    :price: - the necessary money
    :deposit: - money on hand as a percentage of the loan
    :term: - years of credit slavery
    """
    if not price or deposit == None or not term:
        return 0
    else:
        P = self.rate_min / 12
        m = term * 12
        result = ((price * (1 - deposit / 100)) * P) / (1 - (1 + P) * (1 - m))
        return round(result, 2)
