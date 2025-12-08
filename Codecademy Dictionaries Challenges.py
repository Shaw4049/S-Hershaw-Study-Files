# Sum Values

# Write your sum_values function here:
def sum_values(my_dictionary):
    total_sum = 0
    for i in my_dictionary.values():
        total_sum += i
    return total_sum
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# We start by creating a variable to keep track of the total. Next, we use the values() function in our for loop in order to iterate through each of the values in the dictionary. 
# Using this, we can access each value and add it to our total variable. At the end of our loop, we return the total.

# Even Keys
# Write your sum_even_keys function here:
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total_sum = 0
  for i in my_dictionary.keys():
    if i%2 == 0:
      total_sum += my_dictionary[i]
  return total_sum

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Similar to the previous problem, we are iterating through our dictionary, except this time we are iterating through the keys instead of the values. 
# In order to get the keys we use the keys() function and to get the value of a key we can use brackets. To test if the key is even we use the modulus operator and test if the remainder is 0 when dividing by 2. 

# Add Ten
# Write your add_ten function here:
def add_ten(my_dictionary):
  for i in my_dictionary.keys():
    my_dictionary[i] += 10
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# We use a for loop to iterate through each key and we access the value using the key. 
# After accessing it, we overwrite the value with the value plus 10. Finally, we return the modified dictionary.

# Values That Are Keys
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      value_keys.append(value)
  return value_keys
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# For this solution, we iterate through every value within the dictionary. In order to check if it is also a key, we can use the in keyword. 
# This checks the value against all of the keys in the dictionary to see if it exists as a key as well. If it does, then we append it to our list of values which are also keys.

# Largest Value
# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:40, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# In order to program the max algorithm using dictionaries, we need to keep track of the max value and the key which is used to access it. 
# We start by using float("-inf") in order to initialize them to the lowest possible value. To retrieve the key and value at the same time, we use the items() function. 
# Inside our loop, we overwrite the current largest value and the key used to access whenever we find a larger value. We return the largest value’s key once we have iterated through the entire dictionary.