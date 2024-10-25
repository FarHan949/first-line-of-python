#(01) List Manipulation:
# Given a list of integers, nums = [3, 6, 2, 8, 4, 10], use a loop to:

# Multiply each element by 2 and store the result in a new list.
# Find all even numbers and add them to a new list.
# Calculate the sum of all numbers in the list.


nums = [3,6,2,8,4,10]

doubled = []

for num in nums:
    doubled.append(num*2)
    # print(doubled)

odd_Number = []

for num in nums:
 if num % 2 == 0:
   odd_Number.append(num)
#    print(odd_Number)


total_sum = 0
 
for num in nums:
  total_sum =  total_sum + num
  # print(total_sum)


# (02) String Manipulation:
# Given a string, text = "Python is fun!", use a loop to:

# Count the number of vowels in the string.
# Reverse the string without using slicing.
# Create a new string with every alternate character of the original string.

text = "PythOn Is fun!"

vowels = 'aeIou'.lower()

count = 0

for char in text:
  if char.lower() in vowels:
    count += 1
    # print(count)

# for reverseSlice in range(len(text)-1, -1, -1):
  # print(text[reverseSlice])


reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

# print("Reversed string:", reversed_text)


reverse1 =  "ez"
reverse2 =  "easy"
# print(reverse1+reverse2)


alternate_chars = ""
for i in range(len(text)):
    if i % 2 == 0:
        alternate_chars += text[i]

# print("Alternate characters:", alternate_chars)



# (03) Dictionary Iteration:
# Given a dictionary, info = {"name": "Alice", "age": 28, "city": "New York", "hobby": "reading"}, use a loop to:

# Print each key-value pair.
# Create a list of all keys that have a string value.
# Count the total number of characters in all string values.)


info = {
   "name" : "Alice",
   "age" : 28,
   "city" : "New York",
   "hobby" : "reading"
}

for key, value in info.items():
   print(f"{key}: {value}")

new_list = []

# for x in info.keys():
#    new_list.append(x)
#    print(new_list)

for key in info:
    if isinstance(info[key], str):
        new_list.append(key)

# print("Keys with string values:", new_list)



#conform the prime number

# n = int(input("Enter the number:"))

# for i in range(2, n):
#   if n % i == 0:
#       print(n, "is not a prime number")
#       break
# else:
#     print(n, "is a prime number")


#Factorial  of a number
# n = int(input("Enter the number : "))
# product = 1

# for i in range(1, n+1):
#    product =  product * i
#    print(f"The factorial of {n} is {product}")



