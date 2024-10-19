info = {"apple","banana","kiwi", "orange"}

anotherInfo = {"orange","strawberry","blueberries", "banana"}

car = {"Toyota","BMW", "Lamborghini", "banana"} 

normal_dictionary = {
    "name" : "farhan",
    "Age" : 20
}


info.add("jackfruit")   #To add one item to a set use this methods
info.update({"mango","pineapple"})  # to update multiple items to a set use this method
# info.update(normal_dictionary.values())


# print(info.discard("mango"))   #To remove one item from a set use this methods but if the item is not in the set it will return None
# print(info.remove("kiwi"))   #To remove one item from a set use this methods but if the item is not in the set it will raise an error
# pop_method =  info.pop()   #To remove one random item from a set



union_set  = info.union(anotherInfo)  # to get the union of two sets use this method
union_set_operator =  info | anotherInfo | car  # to get the union of two sets use this operator we use to join a multiple sets.but this operator only allowed join sets with sets not with other data types as like union method.


intersection_set =  info.intersection(anotherInfo)  # to get the intersection of two sets use this method and it will return a set with common elements.
                                                     # and we can also use with other data types.
#like list, tuple, dictionary etc.
intersection_set_operator =  info & anotherInfo  # result same like as above method but this operator only allowed join sets with sets not with other data types as like intersection method.

intersection_update_set =  info.intersection_update(anotherInfo)  # to update the set with common elements use this method. modify the original set



difference_set = info.difference(anotherInfo)   # to get the difference of two sets use this method and it will return a set with elements
# difference_update_set = info.difference_update(anotherInfo)  # to update the set with elements that are not in another set use this method. modify the original set
difference_set_operator =  info - anotherInfo  # result same like as above method but this operator only allowed join sets with.


symmetric_difference_set = info.symmetric_difference(car)   # to get the symmetric difference of two sets use this method and it will return a set with  elements
# symmetric_difference_update_set =  info.symmetric_difference_update(anotherInfo)   # to update the set with symmetric difference use this method. modify original set
symmetric_difference_set_operator =   info ^ anotherInfo  # result same like as above method but this operator only allowed join sets with sets


# print(info)
# print(anotherInfo)
print(symmetric_difference_set)



