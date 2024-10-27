# Function definition
def func1():
    print("Hello")

def average ():
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    c = int(input("Enter the number : "))

    avg = ( a + b + c ) / 3
    # print("Average of the numbers is : ", avg)
    return f"Average of the numbers is : , {avg}"


# Function Call
# average()
# func1()

def greet(name, ending="Thank you"):
    return (f"Have a Good day , {name},  {ending}")


a1 = average()
a = greet("Farhan")

print(a1)
print(a)