# 1.Arithmetic Operators: +, -, *, /, //, %, **
a = 15
b = 4

print("Arithmetic Operators:")

print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)  
print("Division:", a / b) 
print("Floor Division:", a // b)  
print("Modulus:", a % b) 
print("Exponentiation:", a ** b)


# 2.Comparison Operators: ==, !=, >, <, >=, <=
a1 = 10
b1 = 20

print("\nComparison Operators:")
print(a1 > b1)
print(a1 < b1)
print(a1 == b1)
print(a1 != b1)
print(a1 >= b1)
print(a1 <= b1)


# 3.Logical Operators: and, or, not
a2 = True
b2 = False

print("\nLogical Operators:")
print("a2 and b2:", a2 and b2)
print("a2 or b2:", a2 or b2)
print("not a2:", not a2)


# 4.Bitwise Operators: &, |, ^, ~, <<, >>
a3 = 5  # 0101 in binary
b3 = 3  # 0011 in binary

print("\nBitwise Operators:")
print("a3 & b3:", a3 & b3)  # Bitwise AND
print("a3 | b3:", a3 | b3)  # Bitwise OR
print("a3 ^ b3:", a3 ^ b3)  # Bitwise XOR
print("~a3:", ~a3)          # Bitwise NOT
print("a3 << 1:", a3 << 1)  # Left Shift
print("a3 >> 1:", a3 >> 1)  # Right Shift


# 5.Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=
a4 = 10

print("\nAssignment Operators:")
a4 += 5
print("a4 += 5:", a4) 

a4 -= 3
print("a4 -= 3:", a4)

a4 *= 2
print("a4 *= 2:", a4)

a4 /= 4
print("a4 /= 4:", a4)

a4 //= 2
print("a4 //= 2:", a4)

a4 %= 3
print("a4 %= 3:", a4)

a4 **= 2
print("a4 **= 2:", a4)



# 6.Identity Operators: is, is not
a5 = 34
b5 = 98
c = a5

print("\nIdentity Operators:")
print("a5 is b5:", a5 is b5)
print("a5 is not b5:", a5 is not b5)
print("a5 is c:", a5 is c)


# 7.Membership Operators: in, not in
list1 = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print("2 in list1:", 2 in list1)
print("6 not in list1:", 6 not in list1)



# 8.Conditional Operator (Ternary Operator): condition_if_true if condition else condition_if_false
x,y = 10, 20
print("\nTernary Operator:")

min = x if x < y else y
print("Minimum of x and y:", min)

# 9. Operator Precedence

print("\nOperator Precedence:")
print("Result of 10 + 20 * 30:", 10 + 20 * 30)  # Multiplication has higher precedence
print("Result of (10 + 20) * 30:", (10 + 20) * 30)  # Parentheses change precedence
print("Result of 10 + 20 - 5 * 2:", 10 + 20 - 5 * 2)  # Multiplication before addition and subtraction
