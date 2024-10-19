a = int(input("Enter the age of the first person: "))

if  a > 18 and  a % 2 != 0:
   print("The first person is an adult and odd age")

elif a== 18 :
    print("Congrats you are the adult now")

elif a<0:
    print("Invalid age")

elif a > 18 and  a % 2 == 0:
    print("The first person is an adult and even age")
    
elif a < 10 or  a == 0:
    print("The first person is a minor and 0 to 10 is not a valid age")

else :
    print("The first person is a minor")




