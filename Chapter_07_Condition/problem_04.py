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


#(04) write a program to find out whether a student has passed or failed it required total of 40% at least 33% in each subject.
    #Assume 3 subjects and take a mark as an input the user.

marks1 = int(input("Enter the marks of student1:"))
marks2 = int(input("Enter the marks of student2:"))
marks3 = int(input("Enter the marks of student3:"))


total_percentage = (100 * (marks1 + marks2 + marks3)) / 3

if  (total_percentage >= 40 and  marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are the passed", total_percentage)

else:
    print("You are failed", total_percentage)



#(05) spam comment defined as a text containing following keyword:

p1 = "make a lot of money"
p2 = "buy this"
p3 = "you will be rich"
p4 = "subscribe this"


message = input("Enter your comment: ").lower()

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):

   print("This comment is a spam")
else:
    print("This comment is not a spam")

