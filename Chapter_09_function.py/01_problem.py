# write a program using function to find the greatest of three number.

def  greatest_of_three(num1, num2, num3):
    if num1 > num2 and num1 >  num3:
        return num1
    elif num2 > num1 and num2> num3:
        return num2
    elif num1 ==  num2 == num3:
       return "All numbers are equal"
    else:
        return num3
    
a  = int(input("Enter the first number:"))
b  = int(input("Enter the second number:"))
c  = int(input("Enter the third number:"))

print(f"the greatest number is : {greatest_of_three(a,b,c)}")


# write a program using function to convert temperature from celsius to fahrenheit.

def celsius_to_fahrenheit(celsius):
    return celsius  * 9/5 + 32

# fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return  (fahrenheit - 32) * 5/9


print(celsius_to_fahrenheit(5))


#  write a program using recursion function to calculate the sum of first n natural numbers.

def sum(n):
    if n == 1:
        return 1
    return  sum(n-1) + n

print(sum(5))





