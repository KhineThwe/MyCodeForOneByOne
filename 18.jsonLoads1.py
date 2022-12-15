#json java script object notation  ------> data format တစ်ခုပဲ
#api exchange တွေမှာအရမ်းအသုံးဝင်တယ်
#ph မှာဖွင့်လိုက်တာနဲ့ weather အချက်အလက်တွေမြင်နေရတာက Server ကနေ api link အနေနဲ့ mobile ph ကိုလှမ်းပေးတာ ကြားထဲမှာ သုံးတဲ့ data
#format ကများသောအားဖြင့် json
#server နဲ့ client အကြား
#Json အပြင် HTML,Plaintext,XML,Json စသဖြင့်ရှိတယ်
#HTML ဆိုရင် data + structure ပါပါနေတယ်
#Plaintext ka tok data plshi ပေမဲ့ လွယ်လွယ်ကူကူ parsing လုပ်လို့မရဘူး
#XML Extensable market language ---> XML parser needed ---> data only pass
#Data pl pass json ll ---> machine yaw lu tway yaw readable phyit tal
#key,value shi tal python dictionary nae tu tal
import json
myJson = """{
 "name" : "khine",
 "age": 25,
 "hobby":["coding","training","building iot"]
}"""

data = json.loads(myJson)
#obj တစ်ခု parameter အနေနဲ့ထည့်ပေးရမယ်
#convert from json to python
#return python dictionary
print(data,type(data))
for key,value in data.items():
    print(value)
print(data['name'])
#load method ကကျ file တွေထဲကနေသွားဖတ်ချင်ရေးချင်တဲ့အချိန်မျိုးမှာ အသုံးပြုတယ်
