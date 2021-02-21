# Dictionary
# using .update() you can add multiple keys
# using .get() for access a dictionary if exists, we can use default value.
# using .pop() for removing items
# using .keys() for accessing all keys
# using .values()
average_age_of_class = {"Jack": 20, "Mark": 25, "Melissa": 23, "Reena": 28}
average_age = 0
for age in average_age_of_class.values():
    average_age += age/ len(average_age_of_class)
print(average_age)

# Using .items()
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Amazon": 64.8}
 
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")

