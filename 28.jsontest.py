#dumps vs loads
#dump ko file nae twal use
#dumps ka python obj parameter
import json
myJson = {
   "name":"Khine Zar Thwe",
    "age":25,
    "hobby":[
        "coding",
        "training",
        "building iot"
    ],
    "pro":[
        "engineering",
        "IT",
        "Japanese teacher",
    ]
}
# json_object = json.dumps(myJson,indent=4)
# print(json_object)
# print(type(json_object))
# with open("jdataFile.json","w") as dataFile:
#     json.dump(myJson,dataFile)
#     #file htl data yout-->python obj and file
#     #serialization lote tr
#     #dict to json
# with open("jdataFile.json","r") as dataFile:
#     data = json.load(dataFile)
#     #deserialization lote tr
#     #json to dict
# print(type(data),data)

#dumps vs loads
jData = json.dumps(myJson)
print(jData,type(jData))

pData = json.loads(jData)
print(pData,type(pData))


#python type ----> json value
#dict ----> object
#list ---> array
#str ---> string
#True ---> true
#False ---> false
#None ---> null
