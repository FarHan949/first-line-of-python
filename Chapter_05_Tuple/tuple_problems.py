                            # Problem 1: Tuple Swapping
# You are given a tuple with two elements, (a, b). Swap the values of a and b without 
# using any temporary variables or additional data structures.

a = (5,10)

# Swapping the values
# a = (a[1], a[0])

b = list(a)
b.reverse()
a = tuple(b)
print(a)  


