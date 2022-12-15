#https://jsonlint.com/
#to check valid json
import json
with open("jdataFile.json") as jsFile:
    data = json.load(jsFile)

for i in data['cars']:
    print(i)

with open("newjdataFile.json","w") as jsFile:
    json.dump(data,jsFile,indent=2)
