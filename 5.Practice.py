# Check if a number is positive
num = int(input("Enter a number:"))
res = "Positive" if num > 0 else "Negative"
print(res)


# Check if a student is pass/fail in exam
marks = int(input("Enter student marks: "))
result = "Pass" if marks >= 40 else "Fail"
print(result)


# Check if a user has balance to buy an item
balance = float(input("Enter your balance: "))
price = float(input("Enter the item price: "))
remark = "You can Purchase" if balance >= price else "You can't afford"
print(remark)


# Suggest a mode of transport based on distance
distance = float(input("Enter distance you want to travel: "))
if distance <= 2:
    print("You can go by walk")
elif distance <= 10:
    print("You can travel by bicycle or scooter")
elif distance <= 50:
    print("You can go with any pubic transport")
else:
    print("Consider a train or flight")


# Battery status
battery = int(input("Enter battery percentage: "))
if battery > 80:
    print("Battery Full")
elif battery > 40:
    print("Battery Half")
else:
    print("Battery Low")


# Nested if-else Statement
# Login with username and password
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "Admin":
    if password == "123":
        print("Access Granted")
    else:
        print("Incorrect Password")
else:
    print("Enter correct Username")


# Check exam pass and scholarship eligibility
marks1 = int(input("Enter your Marks: "))
if marks1 >= 50:
    if marks1 >= 85 and marks1 <=100:
        print("Eligible for Scholarship")
    else:
        print("Not Eligible for Scholarship")
else:
    print("Failed")


# Ternary Statement
n = int(input("Enter a number: "))
print("even" if n%2==0 else "odd")


temp = int(input("Enter the temperature: "))
print("Hot" if temp > 25 else "Cool")


# Assign grade
Grade = input("Enter your Grade (S/A/B/C): ").upper()
match Grade:
    case "S":
        print("Super")
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Fail")


# Activity Suggestion based on weather condition
weather = input("Enter the weather (sunny/rainy/cloudy/snowy): ").lower()
match weather:
    case "sunny":
        print("Great day for an picnic!")
    case "rainy":
        print("Stay indoors and read a book.")
    case "cloudy":
        print("Build a snowman or go skiing.")
    case _:
        print("Unknown weather condition.")


# Mobile notification settings based on user profile mode
mode = input("Enter phone mode (silent/vibrate/loud/do not disturb): ").lower()
match mode:
    case "silent":
        print("Notifications are muted.")
    case "vibrate":
        print("Phone will vibrate for notifications.")
    case "loud":
        print("All notifications will play sound.")
    case "do not disturb":
        print("No calls or notifications will come through.")
    case _:
        print("Invalid mode selected.")