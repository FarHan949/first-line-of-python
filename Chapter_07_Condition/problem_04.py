#(04) Check for Element Presence:

# Given a list lst and an element x, use if, elif, else to print:
# "Found" if x is in lst.
# "Not Found" if x is not in lst.



lst = ['x','vowel']
x = 'vowel'
if x in lst:
    print("Found")
else:
    print("Not Found")


# bouse question 
# (01)Classify Number:

# Given a number n, use if, elif, else to:
# Print "Positive" if n is greater than zero.
# Print "Negative" if n is less than zero.
# Print "Zero" if n is zero.

n = -8

if n > 0 :
    print("Positive")
elif n==0 : 
   print("Zero")
else:
    print("negative")



# (02)Find Common Element:

# Given two lists lst1 and lst2, use if to:
# Print "Common Element Found" if there is at least one common element between lst1 and lst2 (you can use set operations).
# Print "No Common Elements" if there isn't.


lst1 = [5,99,87,107,55,66]
lst2 = [77,78,71,16,10]

if set(lst1).intersection(lst2): 
    print("Common Element Found")

else:
  print("No Common Element")   



#(03) Check String Length:

# Given a string s, use if, elif, else to:
# Print "Short" if the length of s is less than 5.
# Print "Medium" if the length of s is between 5 and 10.
# Print "Long" if the length of s is more than 10.


s = "Python"

if len(s) < 5 :
    print("Short")
elif  len(s) < 11 :
    print("Medium")
else:
    print("Long")

