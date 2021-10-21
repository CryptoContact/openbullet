import requests #line:1
import time #line:2
begins =requests .post (url ='https://vice-prod.sdiapi.com/vicePrm/chipotle/chipotle',headers ={'Ocp-Apim-Subscription-Key':'b4d9f36380184a3788857063bce25d6a'})#line:3
print (begins .headers )#line:4
subscription_key ="b4d9f36380184a3788857063bce25d6a"#line:6
s =requests .Session ()#line:8
s .get ('https://vice-prod.sdiapi.com/vicePrm/chipotle/chipotle')#line:10
r =s .get ('https://services.chipotle.com/restaurant/v3/restaurant/950?embed=addresses,directions,realHours,timezone,onlineOrdering,chipotlane,sustainability')#line:11
print (r .text )#line:13
authkey =requests .get ('https://vice-prod.sdiapi.com/vicePrm/chipotle/chipotle')#line:15
print (authkey .text )#line:16
ops =requests .options ('https://services.chipotle.com/auth/v1/customerauth/login')#line:18
print (ops .text )#line:19
print (ops .cookies )#line:20
ops .cookies ['TS01e7114d']#line:21
crack =requests .post ('https://us.gimp.zeronaught.com/__imp_apg__/api/dc/chipotle?key=AIzaSyB-exZrYwkAq07R3W1C3wZ7tiw2czaabMc')#line:22
print (crack .text )#line:23
print (crack .cookies )#line:24
print (crack .headers )#line:25
getauth =requests .get ('https://chipotle.com/libs/granite/csrf/token.json')#line:26
print (getauth .text )#line:27
print (getauth .cookies )#line:28
op =requests .options ('https://imp.zeronaught.com/__imp_apg__/api/imp/v1.0/report/?fq=signin')#line:29
x =requests .get ('http://chipotle.com/order/sign-in')#line:30
print (x .cookies )#line:31
print (x .text )#line:32
s =requests .Session ()#line:35
with requests .Session ()as s :#line:36
    r =s .get ('https://vice-prod.sdiapi.com/vicePrm/chipotle/chipotle')#line:37
    r =s .post ('https://services.chipotle.com/auth/v1/customerauth/login',data ="ShouldTimeout': 'false', 'UserName': '<USER>', 'Password': '<PASS>")#line:38
