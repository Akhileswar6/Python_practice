str2 = "akhileswar"
print(str2[0])
print(str2[-1])
print(str2[1:5])
print(str2[:6])
print(str2[6:])
print(str2[::2])  # Every second character
print(str2[::-1])  # Reverse the string

s = "A" + str2[1:]
print(s)

str3 = "Venkateswara"
print(len(str3))
print(str3.upper())
print(str3.lower())


s1 = "GeeksforGeeks"
print("Geeks" in s1)
print("GfG" in s1)

# Using format method for string formatting
name = "Akhil"
age = 21
print("My name is {} and I am {} years old.".format(name, age))
