import json
person_list =[]
with open("json_fake_data.json") as jsonFile:
    data = json.load(jsonFile)#load and store into var data
    # print(data[0]['name'])
    # print(data[0]['email'])
    # print(data[0]['balance'])

    for item in data:
        name = item['name']
        email = item['email']
        balance = item['balance']

        person = {
            'name': name,
            'email': email,
            'balance': balance
        }  # dictionary
        person_list.append(person)

    print(person_list)
