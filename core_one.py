# Variables in Python
x = 5
y = "Hello Suleman"
print(y, "It is been ", x, " minutes")
print("Hello World!", end=" ")
print("I will print on the same line.")

# Global Variables
global_var = "I am a global variable"

def myFunc():
    global_var = "I am a local variable"
    print('Python and ' + global_var)


myFunc()


print('Python and ' + global_var)

# Using global keyword to change the value of a global variable inside a function

def myGFunc():
    global x
    x = "Beautiful"
myGFunc()
print("Python is " + x)

l = 0

print(type(l))

# Variables
# Basic Input Output
# Data types