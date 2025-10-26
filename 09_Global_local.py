# local variables
def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()
"""print("Outside:", msg)"""  # This will raise an error since msg is not defined outside the function

# global variables
msg = "Hello"
def greet_global():
    print("Inside:",msg)   # Accessing global variable inside the function

greet_global()
print("Outside:",msg)  # Accessing global variable outside the function


def fun():
    print("Inside Function: ", s)

s = "I love Geeksforgeeks"
fun()
print("Outside Function: ", s)


# Modifying Global Variables Inside a Function
def fun():
    global s
    s += "Akhil"
    print(s)
s = "I love Geeksforgeeks "
fun()
print("Outside Function: ", s)
