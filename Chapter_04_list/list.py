fruits = ["apple",  "banana", "cherry", 7, 8, True]


friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])


# list is a mutable
p1 = [1,2,3]
# p2 = p1[:] # copy the list
p2 = p1  # reference to the same list


p1 = [1,2,3]
# p1[0] = 44

# check  reference value are the same
print(p1 == p2)
# check memory reference position are the same
print(p1 is p2)
print(p1)
print(p2)