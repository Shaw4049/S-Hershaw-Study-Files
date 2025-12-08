# Word Length Dict
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  len_dict = {}
  for word in words:
    len_dict[word] = len(word)
  return len_dict
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# To create a new dictionary we set a variable equal to {}. While iterating through each string in our string list, we can add the key and value to our dictionary using this syntax: word_lengths[word] = len(word). 

# Frequency Count
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freq_dict = {}
  for word in words:
    if word not in freq_dict:
      freq_dict[word] = 0
    freq_dict[word] += 1
  return freq_dict

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# To create a new dictionary we set a variable equal to {}. We iterate through each of the strings in the list of strings and check if it is already in our dictionary using the in keyword. 
# If it is not then we add it as a new key-value pair where the value is 0. Regardless of whether the string was already in the dictionary, increase the value by 1. 
# This will make it so all new entries will have a value of 1 and all existing entries will increase their old value by 1.

# Unique Values
# Write your unique_values function here:
def unique_values(my_dictionary):
  unique_items = []
  for value in my_dictionary.values():
    if value not in unique_items:
      unique_items.append(value)
  return len(unique_items)
  # Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# This function has a similar structure to the last one except that the input has been changed to a dictionary. We iterate through each of the values and whenever we 
# find one we have not added to our list already, we add it to the list. After the loop, we return the length of the list since that contains all unique values from the dictionary.

# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

# This function uses two dictionaries instead of one dictionary and one list. We iterate through each of the keys (which are the last names) and store the first letter of the last name in first_letter. 
# We then use similar logic to what we have used before by testing if we have already seen that letter before. If we haven’t seen that letter before, then we add it to our dictionary with a value of 0. 
# Next, we are going to increment the value. Since we know that some people share the last name (as seen by the list of first names in our names dictionary), 
# we are going to increment the value in our letters dictionary by the length of first names that share the last name for our current iteration (key).