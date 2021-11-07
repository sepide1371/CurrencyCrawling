from django.db import models


class CurrentPrice(models.Model):
    # name of currency
    name = models.CharField(max_length=20, verbose_name='نام')
    # price of currency
    amount = models.IntegerField(verbose_name='قیمت')
    # time of currency price crawling
    time = models.DateTimeField(verbose_name="زمان")

    class Meta:
        verbose_name_plural = "قیمت لحظه ای ارز"
        verbose_name = "قیمت لحظه ای ارز"


class UsdEuroRatio(models.Model):
    # ratio of usd to euro
    ratio = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='نسبت دلار به یورو')
    # time of calculate ratio
    time = models.DateTimeField(verbose_name="زمان")

    class Meta:
        verbose_name_plural = "نسبت لحظه ای دلار به یورو"
        verbose_name = "نسبت لحظه ای دلار به یورو"
