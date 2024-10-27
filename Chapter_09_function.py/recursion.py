'''
Factorial(0) = 1 
Factorial(1) = 1 
Factorial(2) = 2 x 1 
Factorial(3) = 3 x 2 x 1 
Factorial(4) = 4 x 3 x 2 x 1 
Factorial(5) = 5 x 4 x 3 x 2 x 1 

Factorial(n) = n x (n-1) x ..... 3 x 2 x 1

Factorial(n) = n *  Factorial(n-1) 


'''

def  factorial(n):
    return n * factorial(n-1) if n > 1 else 1

def  factorial2(n):
    if ( n == 0 or  n == 1):
        return 1
    return n * factorial(n-1) 


n = int(input("Enter the number : "))
n2 = int(input("Enter the number : "))

print(f"Factorial n  = {n} is {factorial(n)}") 
print(f"Factorial n  = {n2} is {factorial2(n)}") 
