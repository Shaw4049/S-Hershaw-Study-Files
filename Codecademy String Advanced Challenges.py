# Check Name
# Write your check_for_name function here:
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# As you can see, this function can be created using one line. The in keyword will return True if the first provided string 
# is within the second. So in this case, we’re checking if name is in sentence. In order to ignore differences in capitalization, 
# we can use the .lower() function which converts all characters to lowercase characters.

# very Other Letter
# Write your every_other_letter function here:
def every_other_letter(word):
    every_other =""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

# In order to alternate which character is added to the every_other string, we use a range of indices which starts at index 0 
# (the beginning of our word) and ends at the end of our word. The third parameter in the range function determines what value to
# increment by. In this case, we want to increment by 2 in order to get every other letter.

# Reverse
# Write your reverse_string function here:
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, 0, -1):
    reverse += word[i]
  return reverse
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# This is similar to the last solution, but our range has been modified in order to start at the last index of the string (length of the string minus one) up to the first index. 
# Since the parameter for the ending index is exclusive we need to provide the index of one more iteration than what we want to stop at. We want to stop at 0, and since we are incrementing by -1, 
# we will set the ending index to -1. Finally, make sure to add the third parameter of -1. This makes us increment by -1 at each step.

# Make Spoonerism
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+ " " + word1[0]+word2[1:]
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# We can accomplish the task in one line by appending and slicing at the same time. We can get the first index of our words by using word1[0] and word2[0] which gets the letter at the first index. 
# In order to get the remaining letters we can use word1[1:] and word2[1:]. This returns all characters in the strings starting with index 1 and on. We concatenate everything together to get the result.

# Add Exclamation !
# Write your add_exclamation function here:
def add_exclamation(word):
  if len(word) < 20:
    while len(word) < 20:
      word += "!"
    return word
  return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

# Could also be written as:
#def add_exclamation(word):
#  while(len(word) < 20):
#    word += "!"
#  return word


# This function shows how we can continuously append to our string based on some condition. In this case, we keep testing the length of the string to see if we should keep going. 
# Once the length has reached 20, either by adding exclamation marks or by already being long, we return the result.