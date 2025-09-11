from collections import defaultdict

    
# Defining the dict and passing lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

# 1. Using List as Default Factory
d = defaultdict(list)

for i in range(5):
    d[i].append(i)
    
print("Dictionary with values as list:")
print(d)


# 2. Using int Default Factory
d = defaultdict(int)
a = [1, 2, 3, 4, 2, 4, 1, 2]
for i in a:

    d[i] += 1
     
print(d)


# 3. Using str Default Factory
sd = defaultdict(str)
sd['greeting'] = 'Hello'
print(sd)