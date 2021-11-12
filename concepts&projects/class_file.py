total = 0
for i in range(5):
    new_number = int (input("Enter a number: "))
    if new_number == 0:
        total += 1
print("You entered a total of ", total,"Zeros")


list1 = []
while True:
    element = input("Enter the element:")
    list1.append(element)
    choice = input("Want to quit? press yes, otherwise No.")
    if choice == "yes":
        break
print("list1 is:", list1)


