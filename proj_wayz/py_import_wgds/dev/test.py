import json
data = {
  "id": "1020933",
  "name": "深圳海航城分店",
  "address": {
  "city": "深圳市",
  "streetAddressLine1": "龙岗区",
  "streetAddressLine2": "零售商区的地上一层自编A106单元",
  "streetAddressLine3": "龙岗街道海航国兴花园海航城商业广场",
  "postalCode": "518000"
  }
}

temp = json.load(data)
print(temp.get('address',{}).get('city',''))