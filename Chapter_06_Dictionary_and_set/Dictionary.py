personInfo = {
    "name": "John",
    "age": 30,
    "job": "programmer",
    "city": "Dhaka",
    "day" : ["saturday", "5 October", 2024]
}

print(personInfo["day"])


#Adding  a new key-value pair to the dictionary
personInfo["email"] = "person@gmial.com"
personInfo["age"] = 85
personInfo["day"] = [10,100,1000]
personInfo["day"][0] = 1

#removes the key-value pair from the dictionary
del  personInfo["day"]
name = personInfo.pop("job")

# print(personInfo)