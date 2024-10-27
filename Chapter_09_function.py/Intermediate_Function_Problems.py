#(01) Count Vowels in a String: Write a function count_vowels(s) that returns 
     # number of vowels (a, e, i, o, u) in a given string s.


def count_vowels(s):
    count = 0
    vowels = 'aeiou'
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

# print(count_vowels("Hello"))     


#(02) Reverse a List: Write a function reverse_list(lst) that takes a list lst as input
     #  and returns the reversed list.

def reverse_List(lst):
    return lst[::-1]

a = [1, 2, 3, 4, 5]
# print(reverse_List(a))



# Check if a Number is Prime: Write a function is_prime(n) that checks if a number n is prime.

def is_prime(n):
    if n <= 1:
        return f"{n} is not a prime number"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime number"
    return f"{n} is a prime number"

# print(is_prime(7))

     
