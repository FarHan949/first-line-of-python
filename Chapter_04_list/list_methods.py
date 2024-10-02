fruits = ['apple','watermelon','banana']
fruits2  = ["kiwi", "orange", "avocado"]

add_fruits = fruits.append('strawberry')  #append method adds an item to the end of the list

concatenate_list = fruits.extend(fruits2)  #extend method adds all items from the list to the end of the list

fruits.insert(1,  'grape')  #insert method inserts an item at the specified position in the list

fruits.remove("orange")   #remove method removes the first occurrence of the specified value

fruits.pop(-1)   #pop method removes the item at the specified position in the list

fruits2.clear()    #clear method removes all items from the list

count_method = fruits.count("apple")  #count method returns the number of occurrences of the specified value in the list

fruits.reverse()   #reverse method reverses the order of the items in the list

index_method =  fruits.index("apple") #index method returns the index of the first occurrence of the specified value in the list

# fruits.sort(reverse=True)   #sort method sorts the items in the list in ascending order and returns None

copy_list =  fruits.copy()  #copy method returns a copy of the list


print(fruits)
# print(fruits2)
print(count_method)
print(index_method)
print(copy_list)

