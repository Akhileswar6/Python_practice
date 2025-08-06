def factorial(n):
    if n == 0:
        return 1
    elif  n == 1:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))  # Output: 120


# tail recursion -> A function is tail-recursive if the recursive call is the last thing the function does.
def tail_factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_factorial(n - 1, acc * n)

print(tail_factorial(4))

# non-tail recursion -> In non-tail recursion, the recursive call is not the last operation — something still has to be done after it returns.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def print_numbers(n):
    if n == 0:  # base case
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)

# Sum of First N Natural Numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))  # Output: 15


def power(a,b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
print(power(2, 3))  # Output: 8
