str2 = "akhileswar"
print(str2[0])
print(str2[-1])
print(str2[1:5])
print(str2[:6])
print(str2[6:])
print(str2[::2])  # Every second character
print(str2[::-1])  # Reverse the string

# String Methods 
str3 = "Venkateswara"
str4 = "       Akhileswar       "
print(len(str3))
print(str3.upper())
print(str3.lower())
print(str4.strip()) # Remove leading and trailing spaces
print(str3.replace("Venkateswara", "College")) # Replace substring
print(str3.split()) # Split into a list of words
print(str3.find("a")) # Find the index of a substring
print(str3.index("Venkateswara")) # Find the index of a substring (raises error if not found)
print(str3.count("a")) # Count occurrences of a character
print(str3.startswith("Ven")) # Check if string starts with a substring
print(str3.endswith("ara")) # Check if string ends with a substring
print(str3.isalpha())
print(str3.isdigit()) 
print(str3.isalnum()) 
print(str3.islower())
print(str3.isupper())
print(str3.isnumeric())
print(str3.isprintable())  
print(str3.isidentifier())
print(str3.capitalize()) # Capitalize the first character
print(str3.title()) # Convert first character of each word to uppercase
print(str3.swapcase()) # Swap case of all characters
print(str3.center(20, '*'))
print(str3.ljust(20, '*'))
print(str3.rjust(20, '*'))


s1 = "GeeksforGeeks"
print("Geeks" in s1)
print("GfG" in s1)

# Using format method for string formatting
name = "Akhil"
age = 21
print("My name is {} and I am {} years old.".format(name, age))

# String Immutability
s = "Akhileswar"
s = "G"+s[1:]
print(s)

# Updating a String
s = "hello geeks"
s1 = "H" + s[1:]
s2 = s.replace("geeks", "GeeksforGeeks")
print(s1)
print(s2)

# Concatenating and Repeating Strings
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2

# Using format()
ex = "My name is {} and I am {} years old.".format("Akhil", 21)
print(ex)

# Using in for String Membership Testing
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)