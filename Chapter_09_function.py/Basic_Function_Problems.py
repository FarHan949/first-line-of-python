#(01)  Sum of Two Numbers: Write a function sum_two_numbers(a, b) 
   # that returns the sum of two numbers.

def sum_two_numbers(a, b):
    return a + b




#(02) Check Even or Odd: Write a function is_even(n) that returns True 
     #if n is even, and False if n is odd.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return  False



# (03) Square a Number: Write a function square(x) that returns the square of a number.

def square(x):
    return x * x



# (04) Check if String is Palindrome: Write a function is_palindrome(s) that checks 
      # if a given string s is a palindrome (ignoring spaces, case, and punctuation).

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned ==  cleaned[::-1]


# print(sum_two_numbers(5,5))
# print(is_even(5))
# print(square(5))
# print(is_palindrome(" A man, a plan, a canal: Panama"))
