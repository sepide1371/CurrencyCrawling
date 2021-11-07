import os

from celery import Celery
# from crawling.views import current_price

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency_crawling.settings")

app = Celery("currency_crawling")
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.beat_schedule = {
#
# }
app.autodiscover_tasks()



# app.conf.beat_schedule = {
#     "see-you-in-ten-seconds-task": {
#         "task": "crawling.tasks.hello_world",
#         "schedule": 10.0
#     }
# }