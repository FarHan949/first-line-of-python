# write a problem to print the following star  pattern :
'''
     *
    ***
   *****    for n = 3

'''


n = int(input("Enter the numbers of star : "))

for i in range(1, n + 1 ):
    print(" " * (n-i), end="")
    print("*" * (2 * i - 1), end="")  # print the star pattern
    print("")




# write a problem to print the following star  pattern :
'''

   *
   **
   ***  for n = 3

'''

n1 = int(input("Enter the numbers of star : "))
for i in range(1, n1 + 1):
    print("*" * i)  # print the star pattern




# write a problem to print the following star  pattern :
'''

  ***
  * *    for n = 3
  ***

'''

n2 = int(input("Enter the numbers of star : "))

for x in range(n2):
    if x == 0 or x == n2 - 1:
        print("*" * n2)
    else:
        print("*" + " " * (n2 - 2) + "*")



# write a problem to print the following star  pattern :
'''

    *
   **
  ***
 ****
*****

'''

for x in range(1, n2+1):
    print(" " * (n2-x) + "*" * x)



