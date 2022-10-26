# In Python, we have the following 4 types of function arguments.
# Default argument.
# Keyword arguments (named arguments)
# Positional arguments.
# Arbitrary arguments (variable-length arguments *args and **kwargs )

#1.Default arguments
# Python program to demonstrate
# default arguments


def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)


# Driver code (We call myFun() with only
# argument)
myFun(10)

#Keyword argument
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
	print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

