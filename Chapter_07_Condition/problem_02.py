#(02) Check for Subset using Condition method. Given two sets set1 and set2, 
# use if statements to determine and print:
# "set1 is a subset of set2" if set1 is a subset of set2.
# "set2 is a subset of set1" if set2 is a subset of set1.
# "Neither is a subset of the other" if neither is a subset of the other.


set1 = {'a','b','c'}
set2 = {'x',1,5,'j','a','y','b','w','c'}

if set1.issubset(set2)  == True:
    print("set1 is a subset of set2")
elif set2.issubset(set1) == True:
    print("set2 is a subset of set1")
else:
    print("Neither is a subset of the other")



