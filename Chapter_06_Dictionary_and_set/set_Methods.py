info = {"apple","banana","kiwi"}

anotherInfo = {"orange","strawberry","blueberries"}

normal_dictionary = {
    "name" : "farhan",
    "Age" : 20
}


info.add("jackfruit")   #To add one item to a set use this methods

info.update({"mango","pineapple"})  # to update multiple items to a set use this method

# info.update(normal_dictionary.values())

union_set  = info.union(anotherInfo)  # to get the union of two sets use this method
union_set_operator =  info | anotherInfo  # to get the union of two sets use this operator we use to join a multiple sets.but this operator only allowed join sets with sets not with other data types as like union method.


intersection_set =  info.intersection(anotherInfo)  # to get the intersection of two sets use this method and it will return a set with common elements.
                                                     # and we can also use with other data types.

#like list, tuple, dictionary etc.
intersection_set_operator =  info & anotherInfo  # result same like as above method but this operator only allowed join sets with sets not with other data types as like intersection method.




# print(info)
# print(anotherInfo)
print(union_set)



