#(01) Find Common Elements in Two Lists: Write a function common_elements(lst1, lst2)
     # that returns a list of elements that are common between lst1 and lst2.

def common_elements(lst1, lst2):
    return list(set(lst1).intersection(set(lst2))) 



lst1 = [55,66,78,77]
lst2 = [5,66,78,7]

# print(common_elements(lst1,lst2))

#(02) Sort a List of Tuples: Write a function sort_tuples_by_second(lst) that takes a list of 
  # tuples as input and returns a new list of tuples sorted by the second element of each tuple.

def sort_tuples_by_second(lst):
    return sorted(lst, key=lambda x: x[1])

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# print(sort_tuples_by_second(people))


#  Write a function fibonacci(n) that takes an integer n as input and 
# returns the nth Fibonacci number.

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))


           

        
        
               


