# Function declaration by using def keyword
def function():
    print("This is first function")


# Function calling by using function name
function()


# function with arguments : arguments are local variables to the function

def function1(name):
    print("good morning : ", name)


def function2(age, name):
    print("good evening : ", age, name)


function1("test")
function2(12, "test")

name = "Sanjay"  # Global variable


def function3():
    name = "Kumar"  # Local variable


# local vs. global variables : same variable name
# if the application contains both local & global variables same name then to represent global variables
# use global() function

a, b = 10, 20


def sum_local(a, b):
    print(a + b)


def sum_global():
    print(globals()['a'] + globals()['b'])


sum_local(10, 11)
sum_global()


def display():
    global name
    name = "it-test"
    print(name)


display()
print(name)


# Inner function : declaring function inside the another function
def outer():
    print("Outer function")

    def inner():
        print("inner function")

    inner()  # calling inner function


outer()  # calling outer function
