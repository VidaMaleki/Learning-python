num_parties = 3

item_names = ['tickets', 'cotton_candy', 'small_curly_fries', 'large_curly_fries', 'many tickets', 'much cotton candy', 'many small curly fries', 'many large curly fries']
item_vals = [35.00, 1.25, 2.50, 4.00, 112.00]

parties_dict = {}

single_ticket = 35.00
bundle_tickets = 112.00
cotton_candy = 1.25
curly_fries_small = 2.50
curly_fries_large = 4.00

for i in range(num_parties):
  current_party = 'party' + str(i + 1)
  parties_dict[current_party] = {}
  parties_dict[current_party]['bill'] = 0
  parties_dict[current_party]['bundle_tickets'] = 0
  for j in range(len(item_names) - 4):
    while True:
      current_item_val = input("(" + current_party + ")" + " Enter how " + item_names[j + 4] + " you would like to purchase for your party: \n")
      if current_item_val.isdigit():
        break
      else:
        print("That's not a valid input! Try again.")
    parties_dict[current_party][item_names[j]] = int(current_item_val)
    if parties_dict[current_party]['tickets'] >= 4 and j == 0:
      parties_dict[current_party]['bundle_tickets'] = parties_dict[current_party]['tickets'] // 4
      parties_dict[current_party]['tickets'] = parties_dict[current_party]['tickets'] % 4
      parties_dict[current_party]['bill'] += parties_dict[current_party]['bundle_tickets'] * item_vals[-1]
    parties_dict[current_party]['bill'] += parties_dict[current_party][item_names[j]] * item_vals[j]

party_totals = []
concessions_total = []

for i in range(num_parties):
  current_party = 'party' + str(i + 1)
  current_party_readable = 'Party ' + str(i + 1)
  print(str(current_party_readable) + " bought: \n" + str(parties_dict[current_party]['tickets']) + " regular ticket(s) for a price of $" + str(parties_dict[current_party]['tickets'] * item_vals[0]) + "\n" + str(parties_dict[current_party]['bundle_tickets']) + " bundle ticket(s) (4 tickets for $112.00) for a price of $" + str(parties_dict[current_party]['bundle_tickets'] * item_vals[-1]) + "\n" + str(parties_dict[current_party]['cotton_candy']) + " cotton candy serving(s) for a price of $" + str(parties_dict[current_party]['cotton_candy'] * item_vals[1]) + "\n" + str(parties_dict[current_party]['small_curly_fries']) + " small curly fries for a price of $" + str(parties_dict[current_party]['small_curly_fries'] * item_vals[2]) + "\n" + str(parties_dict[current_party]['large_curly_fries']) + " large curly fries for a price of $" + str(parties_dict[current_party]['large_curly_fries'] * item_vals[3]) + "\nThe total for " + str(current_party_readable) + " is $" + str(parties_dict[current_party]['bill']) + "\n")

  party_totals.append(parties_dict[current_party]['bill'])

  for i in range(1,len(item_names) - 4):
    concessions_total.append(parties_dict[current_party][item_names[i]])

print("Total earnings: $" + str(sum(party_totals)))
print("Total earnings from concessions: $" + str(sum(concessions_total)))
print("The most expensive party was: " + "Party " + str(party_totals.index(max(party_totals)) + 1))
