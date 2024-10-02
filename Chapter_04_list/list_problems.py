#(01)  Sum of All Elements
# Given a list lst of integers, calculate and print the sum of all elements.

numbers = [1,2,3,4,5]

print(sum(numbers))



#(02)   Find Maximum and Minimum
# Given a list lst of integers, find and print the maximum and minimum values.

numbers_1 = [1,5,25,23,7,9]

max_number = max(numbers_1)
min_number = min(numbers_1)

print(f"max number is : {max_number}  and min number is : {min_number}")


#(03)   Remove Duplicates from List
# Given a list lst of integers, remove all duplicate elements and print the resulting list.

numbers_2 = [1, 2, 2, 3, 4, 4, 5]
print(list(set(numbers_2)))



#(04)  Concatenate Two Lists
# Given two lists lst1 and lst2, concatenate them into a single list and print the result.

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

concatenate = lst1.extend(lst2)

print(lst1)
