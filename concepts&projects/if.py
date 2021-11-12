print("Example (1) ")
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plany of water")
elif is_cold:
    print("It's a clod day")
    print("Wear worm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

print("\nExample (2)\n")
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

print("\nExample (3).... Logical operators\n")
has_high_income = True 
has_good_credit = True 
has_criminal_record = False
#if has_high_income and has_good_credit:
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

print("\nExample (4).... Comparision Operation\n")

temperature = 40
if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

print("\nExample (5) \n")
characters_limit = 3
name = 'vida'
if len(name) < characters_limit:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")
