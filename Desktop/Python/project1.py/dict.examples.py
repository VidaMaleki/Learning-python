# using function for sum of values
def sum_values(my_dictionary):
    count = 0
    for value in my_dictionary.values():
        count += value
    return count

print(sum_values({"milk":5, "eggs":2, "flour": 3}))

# even keys... sum of the values of all even keys
def sum_even_keys(my_dictionary):
  count = 0
  for key, value in my_dictionary.items():
    if key % 2 == 0 :
      count += value
  return count

print(sum_even_keys({1:5, 2:2, 3:3}))

# Add 10
def add_ten(my_dictionary):
  for key, value in my_dictionary.items():
    my_dictionary[key] = value + 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))

# values that are keys
def values_that_are_keys(my_dictionary):
  list_same_value = []
  for key in my_dictionary.keys():
    for value in my_dictionary.values():
      if key == value:
        list_same_value.append(value)
  return list_same_value

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))

# largest value
def max_key(my_dictionary):
  largest_value = [(value, key) for key, value in my_dictionary.items()]
  return max(largest_value)[1]
  
print(max_key({1:100, 2:1, 3:4, 4:10}))

# word length dict
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

print(word_length_dictionary(["apple", "dog", "cat"]))

# frequency count
def frequency_dictionary(words):
  count = {}
  for word in words:
    if word in count:
      count[word] += 1
    else:
      count[word] = 1
  return count

print(frequency_dictionary(["apple", "apple", "cat", 1]))

# unique values
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
     seen_values.append(value)  
  return len(seen_values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))

# count first letters
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))