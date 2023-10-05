import json

sampleJson = '{"name": "John", "age": "30", "city": "New York City"}'


parsedJson = json.loads(sampleJson)
print("The output of json file is ", parsedJson)
print("Age:", parsedJson["age"])
print("Name: ", parsedJson["name"])
print("City: ", parsedJson["city"])
