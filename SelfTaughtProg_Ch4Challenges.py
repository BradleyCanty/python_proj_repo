# 'The Self-taught Programmer' Ch 4: Functions Challenges
# C1: Write a function that takes a # as input and returns that number squared
print("Ch 5 Challenge 1")
def squareOfNum(x):
    """
    Return the square of x
    :param x: int
    :return: x**2
    """
    return x**2
y = 5
print("The square of " + str(y) + " is " + str(squareOfNum(y)))

# C2: Create a function that accepts a string as a parameter and prints it
print("Ch 5 Challenge 2")
z = "Hello World!"
def strFxn(x):
    """
    Print x to console
    :param x: is int, float, or string
    """
    print(x)
strFxn(z)

# C3: Write a function that takes 3 required parameters & 2 optional parameters
print("Ch 5 Challenge 3")
def fiveParamFxn(x,y,z,alpha=0,beta=0):
    """
    Return the addition of x, y, z, alpha, & beta
    :param x: int or float
    :param y: int or float
    :param z: int or float
    :param alpha: optional int or float; default is 0
    :param beta: optional int or float; default is 0
    :return: 
    """
    return(x+y+z+alpha+beta)
print(fiveParamFxn(1,1,1,1,1))

# C4: Write a program with 2 functions. The 1st function should take an integer
# as a parameter and return the result of the integer divided by 2. The 2nd
# function should take an integer as a parameter and return the result of the
# integer multiplied by 4. Call the 1st function, save the result as a variable,
# & pass it as a parameter to the 2nd function.
print("Ch 5 Challenge 4")
def fxnOne(x):
    """
    Returns x/2
    :param x: int
    :return: x/2
    """
    return x/2
def fxnTwo(y):
    """
    Returns y multiplied by 4
    :param y: int
    :return: y*4
    """
    return y*4
val1 = fxnOne(5)
val2 = fxnTwo(val1)
print(val2)
    

# C5: Write a function that converts a string to a float & return the result. use
# exception handling to catch the exception that could occur.
print("Ch 5 Challenge 5")
def strToFloat(myStr):
    """
    Returns the input string as a float
    :param myStr: string
    :return: float
    """
    return float(myStr)

inputStr = input("Input a number: ")
try:
    print("The float number is: " + str(strToFloat(inputStr)))
except(ValueError):
    print("Invalid input.")

try:
    myValue = 1/0
except(ZeroDivisionError):
    print("Cannot divide by zero")


# C6: Add a docstring to all of the functions above
print("Ch 5 Challenge 6")


