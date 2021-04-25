#String
# string.upper()
# string.lower()
#string.title()
#string.find()
#string.replace( , )
# 'character' in string
# How to use first three letter of names for work username
first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name, last_name):
  new_account = first_name[0:3] + last_name[0:3]
  return new_account
new_account = account_generator("Julie", "Blevins")
print(new_account) # output will be 'JulBle'

# how to choose word from end
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2] # output is 'f'
final_word = company_motto[-4:] # output is 'life'

# how to replace or fix letter
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name) # output 'Rob'

# checking character in word
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False
print(letter_check("vida", "i"))

# common letters
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
print(common_letters('blue', 'blueberry')) # output is ['b', 'l', 'u', 'e']

# making user_name and password with your name
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
print(username_generator('Vida', 'Maleki')) # output is VidMale
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
print(password_generator('VidMale')) # output is eVidMal

# count letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques
print(unique_english_letters("Apple")) # output is 4

# count X
def count_char_x(word, x):
  count = 0
  for i in word:
    if i == x:
      count += 1
  return count

print(count_char_x("mississippi", "s")) # should print 4

# count multi X
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

print(count_multi_char_x("mississippi", "iss")) # should print 2

# substring between letters
def substring_between_letters(word, start, end):
  start_in = word.find(start)
  end_in = word.find(end)
  if start_in > -1 and end_in > -1:
    return word[start_in+1:end_in]
  return word

print(substring_between_letters("apple", "p", "e")) # should print "pl"

# check Name
def check_for_name(sentence, name):
    return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie")) # should print True
print(check_for_name("My name is jamie", "Jamie")) # should print True
print(check_for_name("My name is Samantha", "Jamie")) # should print 

# every other letter
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

print(every_other_letter("Codecademy")) # should print Cdcdm

# Reverse
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

print(reverse_string("Codecademy")) # should print ymedacedoC

# Spoonerism
def make_spoonerism(word1, word2):
    return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print(make_spoonerism("Codecademy", "Learn")) # should print Lodecademy Cearn

# Add exclamation
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

print(add_exclamation("Codecademy")) # should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn")) # should print Codecademy is the best place to learn