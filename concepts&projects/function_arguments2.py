#example 1
numbers  = {'num1': 3, 'num2': 6, 'num3': 9}
 
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
 
sum(**numbers) # 18

#example2
start_and_stop = [3, 6]
 
range_values = range(*start_and_stop)
print(list(range_values)) #[3, 4, 5]

#- Unpacking parts of an iterable
a, *b, c = [3, 6, 9, 12, 15]
print(b) #[6, 9, 12]

#- Merging iterables
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple) #(0, 3, 6, 9, 12)

#Combining unpacking and packing
num_collection = [3, 6, 9]
 
def power_two(*nums): 
  for num in nums:
    print(num**2)
 
power_two(*num_collection)
# 9 
# 36
# 81


def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)

# Write your code below: 
table_7_total = [534.50, 20.0, 5]
calculate_price_per_person(*table_7_total)


