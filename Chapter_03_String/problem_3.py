''' (01)  write a python program to display a users entered name followed by good afternoon 
     using input () function'''

# name  = input("Enter your name: ")

# print(f"Good Afternoon, {name}")  # f-string formatting to insert the name in the string
# print("Good Afternoon, "+ name + "")


print("After the pyhton then the python")  # this is a comment in python


#(02)  Reverse a String
# Given a string s, reverse the string and print the result.

string = "hello"
reversed_string = string[::-1]  # slicing the string from end to start with step -

print(reversed_string)

# (03)  Replace Spaces with Hyphens
# Given a string s, replace all spaces with hyphens (-) and print the result.

string = "this is a test"

print(string.replace(" ", "-"))


# (04)  Count Vowels in a String
# Given a string s, count and print the number of vowels (a, e, i, o, u) in the string.

s = "hello world"

vowel_count = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

print(vowel_count)


#(05)   Check if a String is a Palindrome
# Given a string s, check if the string is a palindrome (reads the same forwards and backwards) and print True if it is, False otherwise.

s1  = "madam"

is_palindrome = s1 == s1[::-1]

print(is_palindrome)


#(06)   Count Occurrences of a Substring
# Given a string s and a substring sub, count and print the number of times sub appears in s.

s2 = "ababab"

sub = "ab"

count_substring =  s2.count(sub)

print(count_substring)



