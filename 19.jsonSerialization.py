# https://docs.python.org/3/library/json.html
#https://jsonlint.com/
#to check valid json 
import json
myJson = {
 "name" : "khine",
 "age": 25,
 "hobby":["coding","training","building iot"]
}#python obj
#convert python obj to json format

#dumps vs dump
#serialization လုပ်တယ်ဆိုတာက python type တွေကနေ json format အဖြစ်သို့ သွား
# ချိန်းတာကိုဆိုလိုခြင်းဖြစ်တယ်

with open("jdataFile.json", "w") as jsFile:
    json.dump(myJson,jsFile)
#dump 2 parameter --- > python obj and json file
