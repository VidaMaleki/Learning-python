#functions are object
# function within function
# Returning functions from functions

def get_math_function(operation): # + or -
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    
    if operation == '+':
        return add
    elif operation == '-':
        return sub
    
add_function = get_math_function('+')
print(add_function(2, 3))
sub_function = get_math_function('-')
print(sub_function(5, 2))