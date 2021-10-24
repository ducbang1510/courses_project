import urllib.request as urllib
import uuid
import hmac
import hashlib
import codecs
import json
from datetime import datetime

endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
secretKey = "YnAUyGXAR5iQ7SibCCtmHcnyk9lHitIN"
accessKey = "H9FWxUZYXUcnjZ0E"

partnerCode = "MOMO3LYS20210822"
requestType = "captureWallet"
redirectUrl = "http://localhost:3000/tour-detail/12/booking-3"
ipnUrl = "http://127.0.0.1:8000/payers/payment/"
orderId = str(uuid.uuid4())
amount = "50000"
orderInfo = "Đơn đặt tour " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
requestId = str(uuid.uuid4())
extraData = ""

rawSignature = "accessKey=" + accessKey + "&amount=" + amount \
               + "&extraData=" + extraData + "&ipnUrl=" + ipnUrl + "&orderId=" + orderId + "&orderInfo=" + orderInfo \
               + "&partnerCode=" + partnerCode + "&redirectUrl=" + redirectUrl + "&requestId=" + requestId \
               + "&requestType=" + requestType

print(rawSignature)

h = hmac.new(codecs.encode(secretKey), codecs.encode(rawSignature), hashlib.sha256)
signature = h.hexdigest()
print("----------------Signature----------------")
print(signature)

data = {
    'partnerCode': partnerCode,
    'accessKey': accessKey,
    'requestId': requestId,
    'amount': amount,
    'orderId': orderId,
    'orderInfo': orderInfo,
    'redirectUrl': redirectUrl,
    'ipnUrl': ipnUrl,
    'lang': "vi",
    'extraData': extraData,
    'requestType': requestType,
    'signature': signature
}

data = json.dumps(data).encode("utf-8")
clen = len(data)

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Content-Length": clen
}

req = urllib.Request(endpoint, data, headers)
f = urllib.urlopen(req)

res = f.read()
f.close()

print("--------------------response----------------\n")
print(res)

payUrl = json.loads(res)['payUrl']
print(payUrl)
