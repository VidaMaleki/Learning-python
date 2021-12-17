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

# Decorating a function
def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper

def print_my_name():
    print("Vida")
    
decorated_function = title_decorator(print_my_name)
decorated_function()

#Decorators and Decorators with parameter
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor:")
        print_name_function(*args, **kwargs)
    return wrapper


@title_decorator
def print_my_name(name, age):
    print(name + " you are " + str(age))
    

print_my_name("Vida", 35)
