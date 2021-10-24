# coding=utf-8
# Python 3.6

from time import time
import hmac, hashlib, urllib.parse, urllib.request, json

query = '?amount=50000' \
        '&discountamount=0' \
        '&appid=554' \
        '&checksum=ec359685cb75b330a8596f818e803b1786820a2a5e6b31d7a57bafa0085429aa' \
        '&apptransid=211022_beb80b6f-2d09-4b61-94d9-af95be844eca' \
        '&pmcid=38' \
        '&bankcode=' \
        '&status=-59'

config = {
    "appid": 554,
    "key1": "8NdU5pG5R2spGHGhyO99HN1OhD8IQJBn",
    "key2": "uUfsWgfLkRLzq6W2uNXTCxrfxs51auny",
    "endpoint": "https://sandbox.zalopay.com.vn/v001/tpe/getstatusbyapptransid"
}

params = {
    "appid": config["appid"],
    "apptransid": "211022_beb80b6f-2d09-4b61-94d9-af95be844eca"
}

data = "{}|{}|{}".format(config["appid"], params["apptransid"], config["key1"])  # appid|apptransid|key1
params["mac"] = hmac.new(config['key1'].encode(), data.encode(), hashlib.sha256).hexdigest()

response = urllib.request.urlopen(url=config["endpoint"], data=urllib.parse.urlencode(params).encode())
result = json.loads(response.read())

for k, v in result.items():
    print("{}: {}".format(k, v))
