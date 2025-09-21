# Different file mode in python
# mode ============= Description
# "r"   ->   Read-only, raises I/O error if doesn't exist
# "r+"  ->   Read and write, raises I/O error if doesn't exist
# "w"   ->   Write-only, Overwrites file if it exists, creates file if doesn't exist.
# "w+"  ->   Write and read, Overwrites file or creates file if doesn't exist.
# "a"   ->   Append-only, Adds data to end, creates file if doesn't exist.
# "a+"  ->   Append and read, creates file if doesn't exist.
# "rb"  ->   Read-only in binary mode, file must exist.
# "rb+" ->   Read and write in binary mode, file must exist.
# "wb"  ->   Write-only in binary mode, overwrites or creates file.
# "wb+" ->   Write and read in binary mode, overwrites or creates file.
# "ab"  ->   Append-only in binary mode, creates file if doesn't exist.
# "ab+" ->   Append and read in binary mode, creates file if doesn't exist.
# "x"   ->   Create-only, raises file exists error if file exists.
# "x+"  ->   Create and read, raises file exists error if file exists.

# Example of different file modes

# 1. Read mode ('r)
with open ("sample.txt", "r") as file:
    content = file.read()
    print("Read mode content:")
    print(content)

# 2. Write mode ('w')
with open("sample.txt", "w") as file:
    file.write("This content is written in write mode.\n")
    file.write("Previous content is overwritten.\n")

# 3. Append mode ('a')
with open("sample.txt", "a") as file:
    file.write("This content is appended in append mode.\n")
    file.write("Previous content is preserved.\n")

# 4.Binary mode ('b')
with open("Academic.png", "rb") as file:
    data = file.read()
    print("Binary mode read, number of bytes:", len(data))

# 5. Read and Write mode ('r+')
with open("sample.txt", "r+") as file:
    content = file.read()
    file.write("\nThis is a new line")

# 6. Write and Read mode ('w+')
with open("sample.txt", "w+") as file:
    file.write("Hello World!")
    file.seek(0)
    content = file.read()
    print("Write and Read mode content:")
