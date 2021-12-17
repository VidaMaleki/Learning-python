#The four distinct types of namespaces that Python generates:
# Built-In
#- It contains many of the built-in functions we are able to use in our Python programs such as str(), zip(), slice(), sorted(), and many more.
#- It also hosts many of the exceptions that we may encounter in our programs such as 'ArithmeticError', 'IndexError', 'KeyError', and many more.
#- There are even constants like True and False!
print(dir(__builtins__))# CHECK the standard built-in namespace

# Global
print(globals()) #check global namespaces
#example
import random
 
first_name = "Jaya"
last_name = "Bodegard" 
 
def print_variables():
  random_number = random.randint(0,9)
  print(first_name)
  print(last_name)
  print(random_number)
# Local
# Enclosing
