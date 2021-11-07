from django.apps import AppConfig
from .tasks import *

class CrawlingConfig(AppConfig):
    name = 'crawling'
    def ready(self):
        import currency_crawling.celery
