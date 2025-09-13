# for loops
# Print each item in a shopping list
items =input("Enter items separated by commas: ").split(',')
for item in items:
    print("Buy:",item.strip())

# Print squares of numbers from 1 to n
n = int(input("Enter a number:"))
for i in range(1,n):
    print(i**2)


# while loops
# Countdown timer
time = int(input("Enter countdown time in seconds: "))
while time > 0:
    print("Coundown left:",time)
    time -= 1

# Sum until user enters 0
total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print("Total sum:",total)

# Print a multiplication table
n = 3
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
    

# Print Identity Matrix Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()

# Break
# Stop printing at a target item
items = ["apple", "banana", "cherry", "stop", "mango"]
for item in items:
    if item == "stop":
        break
    print("Item:", item)


# Find first even number
while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("First even number found:", num)
        break

# Continue
# Skip out-of-stock items
items = ["milk", "bread", "out of stock", "eggs"]
for item in items:
    if item == "out of stock":
        continue
    print("Buy:", item)

# Skip even numbers
nums = 10
for i in range(1, nums+1):
    if i%2==0:
        continue
    print(i,end=' ')


# pass
tasks = ["email", "meeting", "call"]
for task in tasks:
    if task == "call":
        pass  # Logic to be added later
    print("\nDo:", task)