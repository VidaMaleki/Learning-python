#In Python, a lambda function (also commonly called an anonymous function)
# is a one-line shorthand for function.
add_two = lambda my_input: my_input + 2
print(add_two(3))
print(add_two(100))
print(add_two(-2))

#In the lambda function version,
# we are returning my_input + 2 without the use of a return keyword 
# (the normal Python function explicitly uses the keyword return).

#complex example
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'