#Function Arguments
#1-Positional Arguments
def print_name(first_name, last_name): 
    print(first_name, last_name)
 
print_name('Jiho', 'Baggins')

#2-Keyword Arguments
def print_name(first_name, last_name): 
    print(first_name, last_name)
 
print_name(last_name='Baggins', first_name='Jiho')

#3-Default arguments
def print_name(first_name='Jiho', last_name='Baggins'): 
    print(first_name, last_name)
 
print_name()

#Variable number of arguments: *args
def print_order(*order_items):
    print(order_items)

print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')


#Variable number of arguments: **kwargs
#first example
def arbitrary_keyword_args(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # See if there's an 'anything_goes' keyword arg and print it
    print(kwargs.get('anything_goes'))
 
arbitrary_keyword_args(this_arg='wowzers', anything_goes=101)

#second example
def print_data(**data):
    for arg in data.values():
        print(arg)
 
print_data(a='arg1', b=True, c=100)

#combine our use of ** with regular positional arguments
def print_data(positional_arg, **data):
    print(positional_arg)
    for arg in data.values():
        print(arg)
 
print_data('position 1', a='arg1', b=True, c=100)

#all together
def single_prix_fixe_order(appetizer, *entrees , sides, **dessert_scoops ):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)

single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides = 'Mashed Potatoes',dessert_scoops = "Vanilla, Cookies and Cream"  )