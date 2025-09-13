# If condition

age = 19
if age > 18:
    print("You are an adult.")

# Short Hand if
if age > 18 : print("You are eligible to vote.")


# If-else condition
age = 10
if age <= 12:
    print("Travel for free")
else:
    print("Pay for ticket")

# Short Hand if-else
marks = 45
res = "Pass" if marks >= 40 else "Fail"

print(f"Result: {res}")


# Elif condition
age1 = 25
if age1 <= 12:
    print("Child")
elif age1 <=19:
    print("Teenager")
elif age1 <=30:
    print("Young Adult")
else:
    print("Adult")


# Nested if condition
age2 = 70 
is_member = True
if age2 >=60:
    if is_member:
        print("30% senior discount")
    else:
        print("10% senior discount")
else:
    print("No senior discount available")


# Ternary Conditional Statement
age3 = 19
s = "Adult" if age >=18 else "Minor"
print(f"Status: {s}")


# Match-Case Statement
number = 1
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")