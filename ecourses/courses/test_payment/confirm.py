import urllib.parse
import hmac
import hashlib
import codecs

secretKey = "YnAUyGXAR5iQ7SibCCtmHcnyk9lHitIN"
# url = "http://localhost:3000/tour-detail/12/booking-3?partnerCode=MOMO3LYS20210822&orderId=9ab17509-a8e3-442a-b579-f6ce491e5654&requestId=97abc840-99e4-4406-b50a-dd2afa64d041&amount=50000&orderInfo=%C4%90%C6%A1n%20%C4%91%E1%BA%B7t%20tour%2001/10/2021%2010:47:29&orderType=momo_wallet&transId=2585815105&resultCode=0&message=Giao%20d%E1%BB%8Bch%20th%C3%A0nh%20c%C3%B4ng.&payType=qr&responseTime=1633060069254&extraData=&signature=e6b85e5352fd23d6b4251ec7635106e8e978f0c15ff0516f76e8522ed429e3fe"
#
# param = "accessKey=" + accessKey + "&" + url[url.find("?")+1:url.find("signature")-1]
# param = urllib.parse.unquote(param)
#
# result = url[url.find("resultCode")+11:url.find("resultCode")+12]

accessKey = "H9FWxUZYXUcnjZ0E"
amount = "50000"
extraData = ""
message = "Giao dịch thành công."
          # "Giao%20d%E1%BB%8Bch%20th%C3%A0nh%20c%C3%B4ng."
orderId = "9ab17509-a8e3-442a-b579-f6ce491e5654"
orderInfo = "Đơn đặt tour 01/10/2021 10:47:29"
            # "%C4%90%C6%A1n%20%C4%91%E1%BA%B7t%20tour%2001/10/2021%2010:47:29"
orderType = "momo_wallet"
partnerCode = "MOMO3LYS20210822"
payType = "qr"
requestId = "97abc840-99e4-4406-b50a-dd2afa64d041"
responseTime = "1633060069254"
resultCode = "0"
transId = "2585815105"

param = "accessKey=" + accessKey + \
        "&amount=" + amount + \
        "&extraData=" + extraData + \
        "&message=" + message + \
        "&orderId=" + orderId + \
        "&orderInfo=" + orderInfo + \
        "&orderType=" + orderType + \
        "&partnerCode=" + partnerCode + \
        "&payType=" + payType + \
        "&requestId=" + requestId + \
        "&responseTime=" + responseTime + \
        "&resultCode=" + resultCode + \
        "&transId=" + transId

param = urllib.parse.unquote(param)
signature = hmac.new(codecs.encode(secretKey), codecs.encode(param), hashlib.sha256).hexdigest()

if signature != "e6b85e5352fd23d6b4251ec7635106e8e978f0c15ff0516f76e8522ed429e3fe":
    print("Thong tin request khong hop le")
else:
    print("Thong tin request hop le")
    if resultCode != "0":
        print("Thanh toan that bai")
    else:
        print("Thanh toan thanh cong")
