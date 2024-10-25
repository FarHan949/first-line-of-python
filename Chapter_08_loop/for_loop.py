for i in range(6):
    print(i)


for x in "banana":
  print(x)


fruits = ["apple", "banana", "cherry"]
 
for x in fruits:
   if x == "banana":
      break
  #  print(x)


for y in fruits:
   if y == "banana":
      continue
  #  print(y)


adj = ["red", "big", "tasty"]
fruitsTable = ["orange", "kiwi", "guava"]

# Example of the Nested  Loop
for x in adj:
  for y in fruitsTable:
    print(x,y)

