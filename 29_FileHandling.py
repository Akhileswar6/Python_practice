# Opening a File in Python
# file = open('filename.txt', 'mode')

# Basic Example: Opening a File
# with open("C:/Users/akhil/OneDrive/Desktop/Numpy/codeharry_numpy.py", "r") as f:
#     print(f.read())

# Checking File Properties
f = open("01_Basics.py", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed:", f.closed)

# Closing a File
f.close()
print("Is Closed after closing:", f.closed)

# Reading from a File
file = open("01_Basics.py", "r")
content = file.read()
print(content)
file.close()

# Writing to a File
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Writing to files in Python is easy!")

print("Data written to sample.txt")

# Handling Exceptions when closing a File
try:
    f = open("02_Datatypes.py", "r")
    content = f.read()
    print(content)
finally:
    file.close()