# Arbitary keyword Arguments
# *args -> *argv allows you to pass a variable number of positional arguments to a function and becomes a tuple.
def myFunc(*argv):
    for i in argv:
        print(i)
myFunc("akhil","vishnu","suresh")

def func1(*names):
    for i in names:
        print("Hello " + i)
func1("Akhli", "Vishnu", "Suresh")


# **kwargs -> **argv allows you to pass a variable number of keyword arguments and becomes a dictionary.
def myFunc(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key, value))
myFunc(first="Akhil", mid="for", last="Kamale")

def func2(**info):
    for key,value in info.items():
        print(f"{key} : {value}")
func2(name="Akhil",age=19,country="India")


# combining *argv with extra arguments
def func3(arg1, *argv):
    print("First Arguments:",arg1)
    for i in argv:
        print("Arguments :",i)
func3(12,23,98,"Emotion","Peace")


# combining **argv with extra arguments
def fun(arg1, **kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))
fun("Hi", s1='Geeks', s2='for', s3='Geeks')


# We can combine both
def both(a, *args, **kwargs):
    print("a =",a)
    print("*argv =",args)
    print("**kwargs =",kwargs)
both(12,23,45,name="Abhi",age=12)


