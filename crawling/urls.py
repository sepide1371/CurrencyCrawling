"""currency_crawling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from crawling import views
from crawling.views import UsdEuroRatioList, CurrentCurrencyList, HistoryCurrencyList

urlpatterns = [
    # path("current", views.current_price, name="CurrentPrice"),
    path("history/ratio", UsdEuroRatioList.as_view(), name="UsdEuroRatio"),
    path("current/<str:name>", CurrentCurrencyList.as_view(), name="CurrentCurrency"),
    path("history/<str:name>", HistoryCurrencyList.as_view(), name="HistoryCurrency"),
]
