# coding=utf-8
# Python 3.6

from time import time
from datetime import datetime
import json, hmac, hashlib, urllib.request, urllib.parse, random

config = {
  "app_id": 2554,
  "key1": "sdngKKJmqEMzvh5QQcdD2A9XBSKUNaYn",
  "key2": "trMrHtvjo6myautxDUiAcYsVtaeQ8nhf",
  "endpoint": "https://sb-openapi.zalopay.vn/v2/create"
}
transID = random.randrange(1000000)
print(random.randrange(1000000))
order = {
  "app_id": config["app_id"],
  "app_trans_id": "{:%y%m%d}_{}".format(datetime.today(), transID), # mã giao dich có định dạng yyMMdd_xxxx
  "app_user": "user123",
  "app_time": int(round(time() * 1000)), # miliseconds
  "embed_data": json.dumps({
      "promotioninfo": "",
      "merchantinfo": "embeddata123",
      "redirecturl": "http://localhost:3000/tour-detail/8/booking-3/5/3/confirm",
  }),
  "item": json.dumps([{}]),
  "amount": 50000,
  "description": "Lazada - Payment for the order #"+str(transID),
  "bank_code": "zalopayapp"
}

# app_id|app_trans_id|app_user|amount|apptime|embed_data|item
data = "{}|{}|{}|{}|{}|{}|{}".format(order["app_id"], order["app_trans_id"], order["app_user"], 
order["amount"], order["app_time"], order["embed_data"], order["item"])

order["mac"] = hmac.new(config['key1'].encode(), data.encode(), hashlib.sha256).hexdigest()

response = urllib.request.urlopen(url=config["endpoint"], data=urllib.parse.urlencode(order).encode())
result = json.loads(response.read())

return_code = result['return_code']
order_url = result['order_url']
print(return_code)
print(order_url)
# for k, v in result.items():
#   print("{}: {}".format(k, v))