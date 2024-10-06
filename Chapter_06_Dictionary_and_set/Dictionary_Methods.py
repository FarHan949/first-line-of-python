a = {
    "key" :  "value",
    "farhan" : "code",
    "mark": 100,
    "list": [1,2,2]
}


#Adding  a new key-value pair to the dictionary
a["email"] = "person@gmial.com"
a["mark"] = 85


#removes the key-value pair from the dictionary
del  a["list"]
name = a.pop("farhan")

print(a)