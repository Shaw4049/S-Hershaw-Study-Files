# Divisible By Ten
#Write your function here
def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 == 0:
      counter += 1
  return counter
#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# In this solution, we defined the function and set up our counter. We use a for loop to iterate through each number and check if it is divisible by ten. 
# If a number is divisible by another number then the remainder should be zero, so we use modulus. After the loop has finished, we return our count.

# Greetings
#Write your function here
def add_greetings(names):
  greeting_list = []
  for name in names:
   greeting_list.append("Hello, " + name)
  return greeting_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# First, we set up our function to accept the list of strings and we initialized a new list of strings to hold our greetings. 
# We iterate through each name and we append and concatenate the strings at the same time within our loop. Finally, we return the list containing all of our eloquent greetings.

# Delete Starting Even Numbers
#Write your function here
def delete_starting_evens(my_list):
  while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# After defining our method, we use a while loop to keep iterating as long as some provided conditions are true. We provide two conditions for the while loop to continue. 
# We will keep iterating as long as there is at least one number left in the list len(my_list) > 0 and if the first element in the list is even my_list[0] % 2 == 0. 
# If both of these conditions are true, then we replace the list with every element except for the first one using my_list[1:]. Once the list is empty or we hit an odd number, 
# the while loop terminates and we return the modified list.

# Odd Indices
#Write your function here
def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# In our solution, we iterate through a range of values. The function range(1, len(my_list), 2) returns a list of numbers starting at 1, ending at the length of len, and incrementing by 2. 
# This causes the loop to iterate through every odd number until the last index of our list of numbers. 
# Using this, we can simply append the element at whatever index we are at since we know that using our range we will be iterating through only odd indices.

# Another way to do this would be to iterate through all indices and use an if statement to see if the index you’re currently looking at is odd.

# Exponents
#Write your function here
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

# As you can see in this solution, we used two nested for loops so that, for every base, we iterate through every power. 
# This allows us to raise each base to every single power in our list and append the answers to our new list. Finally, we return the list of answers.