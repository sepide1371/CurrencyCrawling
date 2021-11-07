# import datetime
#
# import requests
# from celery import shared_task, Celery
#
# from crawling.models import CurrentPrice, UsdEuroRatio
#
#
# def calculate_ratio(value1, value2):
#     ratio = value1/value2
#     return ratio
#
# app = Celery("currency_crawling")
# @app.task(bind=True)
# def current_price(self):
#     current_info = datetime.datetime.now()
#     current_date = str(current_info).split(" ")[0]
#
#     start_time = current_date + " 09:00:00"
#     start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
#
#     end_time = current_date + " 17:00:00"
#     end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
#
#     if current_info >= start_time and current_info <= end_time:
#         print("check----------------------------")
#         headers = {}
#         url = "https://tgju.org"
#         data = {}
#         try:
#             currency_name_p = ['دلار', 'یورو']
#             currency_name_e = ['usd', 'euro']
#             currency_flag = ['flag-us', 'flag-eu']
#             req_time = datetime.datetime.now()
#             response = requests.request("GET", url, data=data, headers=headers)
#             usd_text = 0
#             euro_text = 0
#             for c in currency_name_e:
#                 idx = currency_name_e.index(c)
#                 search_tag = '<th><span class="mini-flag ' + currency_flag[idx] + '"></span>' + currency_name_p[idx] + '</th>'
#                 search_tag_len = len(search_tag)
#                 start_idx = response.text.find(search_tag)
#                 start = start_idx + search_tag_len + 16
#                 end = start_idx + search_tag_len + 23
#                 currency_amount = response.text[start:end]
#                 if c == "usd":
#                     usd_text = currency_amount
#                 elif c == "euro":
#                     euro_text = currency_amount
#                 else:
#                     pass
#                 currency_amount = int(currency_amount.replace(",", ""))
#                 new_currency = CurrentPrice()
#                 new_currency.time = req_time
#                 new_currency.name = currency_name_e[idx]
#                 new_currency.amount = currency_amount
#                 new_currency.save()
#             if usd_text != 0 and euro_text != 0:
#                 usd_text = int(usd_text.replace(",", ""))
#                 euro_text = int(euro_text.replace(",", ""))
#                 ratio = calculate_ratio(usd_text, euro_text)
#                 new_ratio = UsdEuroRatio()
#                 new_ratio.ratio = ratio
#                 new_ratio.time = req_time
#                 new_ratio.save()
#             print("-------------------- currency updated --------------------")
#             return True
#         except Exception as e:
#             print("-------------------- current price update error --------------------")
#             print(e)
#             return None
#     else:
#         print(current_info)
#         print(start_time)
#         print(end_time)
#         print("out of range --------> ", datetime.datetime.now())
#         return None
