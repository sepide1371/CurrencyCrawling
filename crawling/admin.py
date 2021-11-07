from django.contrib import admin

from crawling import models


@admin.register(models.CurrentPrice)
class CurrencyPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'time',)
    search_fields = ('name', 'amount', 'time',)


@admin.register(models.UsdEuroRatio)
class UsdEuroRatioAdmin(admin.ModelAdmin):
    list_display = ('id', 'ratio', 'time',)
    search_fields = ('ratio', 'time',)
