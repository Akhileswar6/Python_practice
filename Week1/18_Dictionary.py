d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

# create dictionary using dict() constructor with tuples
d3 = dict([(1, 'Geeks'), (2, 'For'), (3, 'Geeks')])
print(d3)

# create dictionary using dict() constructor with list of lists
d4 = dict([[1, 'Geeks'], [2, 'For'], [3, 'Geeks']])
print(d4)




# Accessing Dictionary Items
d5 = { "name": "Prajjwal", 1: "Python", "nums": [1,2,4], "age": 20, "marks": 90.5 }

# Access using key
print(d5["nums"])

# Access using get()
print(d5.get("name"))

# Adding new key-value pair
d5["education"] = "B.Tech"

# Updating an existing value
d5["name"] = "Akhil"
print(d5)



# Removing Dictionary Items
d6 = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d6["age"]
print(d6)

# Using pop() to remove an item and return the value
val = d6.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d6.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d6.clear()
print(d6)



# Iterating Through a Dictionary
d7 = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d7:
    print(key)

# Iterate over values
for value in d7.values():
    print(value)

# Iterate over key-value pairs
for key, value in d7.items():
    print(f"{key}: {value}")