a = {
    "key" :  "value",
    "farhan" : "code",
    "mark": 100,
    "list": [1,2,2]
}


a.update({"name" : "Jonathan", "city": "islamabad"})   #(01) update the dictionary with new key-value pairs

copy_a = a.copy()  #(02) create a copy of the dictionary

clear_a = copy_a.clear()   #(03) clear the dictionary

item_a = a.items()    #(04) get a view object that displays a list of a dictionary’s key-value tuple pairs

value_a = a.values()   #(05) get a view object that displays a list of all values in the dictionary

keys_a = a.keys()     #(06)  get a view object that displays a list of all keys in the dictionary

pop_a = a.pop("list")  #(07) remove the item with the specified key and return the corresponding value.

popItem_a = a.popitem()   #(08) remove and return an arbitrary element from the dictionary.

get_a = a.get("name")    #(09)  return the value for the given key if it exists in the dictionary.

fromkeys_a = dict.fromkeys(a, "unknown")   #(10) create a new dictionary with keys from iterable and values set to value.

setdefault_a = a.setdefault("Location", "Dhaka")   #(11) insert key with a given value if key is not available in dictionary.



print(a)
# print(get_a)
print(fromkeys_a)
# print(setdefault_a)
