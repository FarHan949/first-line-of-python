#(01) Given three numbers a, b, and c, use if, elif, else to print the largest number.

a =  int(input("Enter the number of a :"))
b =  int(input("Enter the number of b :"))
c =  int(input("Enter the number of c :"))

if a > b  and a > c:
    print(a, "is the largest number")

elif b > c and b> a : 
    print(b, "is the largest number")
else:
    print(c, "is the largest number")


