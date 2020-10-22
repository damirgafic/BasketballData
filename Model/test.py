'''
Things to be done:
-scrape all salaries and PER stats

'''


# Python program to demonstrate
# AttributeError


class Geeks():

    def __init__(self):
        self.a = 'GeeksforGeeks'


# Driver's code
obj = Geeks()

# Try and except statement for
# Exception handling
try:
    print(obj.a)

    # Raises an AttributeError
    print(obj.b)

# Prints the below statement
# whenever an AttributeError is
# raised
except AttributeError:
    print("There is no such attribute")
