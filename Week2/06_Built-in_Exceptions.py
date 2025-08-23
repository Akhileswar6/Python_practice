# Exception Name	                      Description
# -------------------            ------------------------------------------------
# BaseException	                     The base class for all built-in exceptions.
# Exception	                         The base class for all non-exit exceptions.
# ArithmeticError	                 Base class for all errors related to arithmetic operations.
# ZeroDivisionError	                 Raised when a division or modulo operation is performed with zero as the divisor.
# OverflowError	Raised               when a numerical operation exceeds the maximum limit of a data type.
# FloatingPointError	             Raised when a floating-point operation fails.
# AssertionError	                 Raised when an assert statement fails.
# AttributeError	                 Raised when an attribute reference or assignment fails.
# IndexError	                     Raised when a sequence subscript is out of range.
# KeyError	                         Raised when a dictionary key is not found.
# MemoryError	                     Raised when an operation runs out of memory.
# NameError	                         Raised when a local or global name is not found.
# OSError	                         Raised when a system-related operation (like file I/O) fails.
# TypeError	                         Raised when an operation or function is applied to an object of inappropriate type.
# ValueError	                     Raised when a function receives an argument of the right type but inappropriate value.
# ImportError                    	 Raised when an import statement has issues.
# ModuleNotFoundError           	 Raised when a module cannot be found.
# IOError	                         Raised when an I/O operation (like reading or writing to a file) fails.
# FileNotFoundError	                 Raised when a file or directory is requested but cannot be found.
# StopIteration                      Raised when the next() function is called and there are no more items in an iterator.
# KeyboardInterrupt                  Raised when the user presses Ctrl+C or interrupts the program’s execution.
# SystemExit	                     Raised when the sys.exit() function is called to exit the program.
# NotImplementedError	             Raised when an abstract method that needs to be implemented is called.
# RuntimeError                       Raised when a general error occurs in the program.
# RecursionError	                 Raised when the maximum recursion depth is exceeded.
# SyntaxError	                     Raised when there is an error in the syntax of the code.
# IndentationError                   Raised when there is an indentation error in the code.
# TabError	                         Raised when the indentation consists of inconsistent use of tabs and spaces.
# UnicodeError	                     Raised when a Unicode-related encoding or decoding error occurs.


# 1.BaseException
try:
    raise BaseException("This is a BaseException")
except BaseException as e:
    print(f"Caught an exception: {e}")

# 2.Exception
try:
    raise Exception("This is a general exception")
except Exception as e:
    print(f"Caught an exception: {e}")

# 3.ArithmeticError
try:
    raise ArithmeticError("Arithmetic error occurred")
except ArithmeticError as e:
    print(f"Caught an arithmetic error: {e}")

# 4.ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught a zero division error: {e}")

# 5.OverflowError
import math
try:
    result = math.exp(1000)  # This will raise an OverflowError
except OverflowError as e:
    print(f"Caught an overflow error: {e}")

# 6.FloatingPointError
import sys
import math
sys.float_info.max = 1.79e+308  # Maximum float value
try:
    math.sqrt(-1.0)  # This doesn't raise a FloatingPointError by default
except FloatingPointError as e:
    print(f"Caught a floating point error: {e}")

# 7.AssertionError
try:
    assert 1 == 2, "Assertion failed"
except AssertionError as e:
    print(e)

# 8.AttributeError
class MyClass:
    pass
obj = MyClass()
try:
    obj.some_attribute
except AttributeError as e:
    print(e)

# 9.IndexError
my_list = [1, 2, 3]
try:
    element = my_list[5]
except IndexError as e:
    print(e)

# 10.KeyError
d = {"key1": "value1"}
try:
    val = d["key2"]
except KeyError as e:
    print(e)

# 11.MemoryError
try:
    li = [1] * (10**10)
except MemoryError as e:
    print(e)

# 12.NameError
try:
    print(var)
except NameError as e:
    print(e)

# 13.OSError
try:
    open("non_existent_file.txt")
except OSError as e:
    print(e)

# 14.TypeError
try:
    result = '2' + 2
except TypeError as e:
    print(e)

# 15.ValueError
try:
    res = int("abc")
except ValueError as e:
    print(e)

# 16.ImportError
try:
    import mod
except ImportError as e:
    print(e)

# 17.ModuleNotFoundError
try:
    import module
except ModuleNotFoundError as e:
    print(e)

# 18.IOError
try:
    open("non_existent_file.txt")
except IOError as e:
    print(e)

# 19.FileNotFoundError
try:
    open("non_existent_file.txt")
except FileNotFoundError as e:
    print(e)

# 20.StopIteration
my_iter = iter([1, 2, 3])
try:
    while True:
        print(next(my_iter))
except StopIteration as e:
    print("End of iterator")

# 21.KeyboardInterrupt
try:
    while True:
        pass
except KeyboardInterrupt as e:
    print("Program interrupted by user")

# 22.SystemExit
import sys

try:
    sys.exit()
except SystemExit as e:
    print("System exit called")