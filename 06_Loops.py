# for loop
n = 4
for i in range(0, n):
    print(i)

lst = ["Geeks", "for", "Geeks"]
for i in lst:
    print(i)

tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)

s = "Geeks"
for i in s:
    print(i)

d = dict({'x':123, 'y':354})
for j in d:
    print("%s  %d" % (j, d[j]))

set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)


# loop through string
for char in "hello":
    print(char)

# Iterating by the Index of Sequences
li = ["Geeks","for","Geeks"]
for i in range(len(li)):
    print(li[i])

# Using else Statement with for Loop in Python
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])
else:
    print("Inside Else Block")

# sum of first 5 numbers
total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)

# Loop with enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Reverse loop
for i in range(5,0,-1):
    print(i)


# while loop
cnt = 1
while (cnt < 3):
    cnt +=1
    print("Akhil")

# Using else statement with While Loop
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
else:
    print("In Else Block")


# Nested Loops
for i in range(1,6):
    for j in range(i):
        print(i, end=' ')
    print()


# Break Statement
for letter in "Python":
    if letter == 'h':
        break
    print(letter, end=' ')
print()

# Continue Statement
for letter in "Akhileswar":
    if letter == 'e':
        continue
    print(letter, end=' ')
print()

# Pass Statement
for letter in "Akhileswar":
    if letter == 'i':
        pass 
    print(letter, end=' ')
