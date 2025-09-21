# Basic file reading

# Open the file in read mode
file = open("sample.txt", "r")

# Read the entire content of the file
content = file.read()
print("File Content:\n")
print(content)

# Close the file
file.close()


# Best Practice: Using with statement
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content using with statement:\n")
    print(content)


# Reading a file line by line
# 1.Using a Loop to Read Line by Line
file = open("sample.txt", "r")
for line in file:
    print("=====================")
    print("line:", line.strip())
file.close()

# 2.Using readline()
file = open("sample.txt", "r")
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()


# Reading Binary Files
file = open("Academic.png", "rb")
data = file.read()
print("Number of bytes read from binary file:", len(data))
print(data)
file.close()



# Writing to a File in python
with open("file.txt", "w" , encoding="utf-8") as file:
    file.write("The only way to do great work is to love what you do. - Steve Jobs\n")
    file.write("Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill\n")
    file.write("Believe you can and you're halfway there. - Theodore Roosevelt\n")
    file.write("Don't watch the clock; do what it does. Keep going. - Sam Levenson\n")
   
with open("file.txt", "r", encoding="utf-8") as file:
    print(file.read())


# Appending to a existing file
with open("file.txt", "a", encoding="utf-8") as file:
    file.write("Your time is limited, so don't waste it living someone else's life. - Steve Jobs\n")
    file.write("The best way to predict the future is to invent it. - Alan Kay\n")

with open("file.txt", "r", encoding="utf-8") as file:
    print(file.read())


# Create only if it does not exist
try:
    with open("file.txt", "x", encoding="utf-8") as f:
        f.write("Created using exclusive mode.\n")
except FileExistsError:
    print("file.txt already exists, exclusive creation aborted.")


# Writing multiple lines
# Example 1: This writes a list of lines; each element includes a \n.
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("file1.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

with open("file1.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Example 2: join + single write (often cleaner)
lines = ["Line A", "Line B", "Line C"]
text = "\n".join(lines) + "\n"
with open("file2.txt", "w", encoding="utf-8") as f:
    f.write(text)

with open("file2.txt", "r", encoding="utf-8") as f:
    print(f.read())