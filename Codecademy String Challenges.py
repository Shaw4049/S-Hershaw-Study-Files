letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
# I created a count variable and set to zero, and an empty list, then iterated through each letter of the word. If the letter was in the 
# provided letters variable and was not in the unique_letters list, append the unique_letter list with the current iterated letter then add 1 
# to the total count. 
def unique_english_letters(word):
  count = 0
  unique_letters = []
  for letter in word:
    if letter in letters and letter not in unique_letters:
      unique_letters.append(letter)
      count += 1
  return count
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters("Zoe Broom"))
# should print 6

# The simpler method to do this:
# Iterate through the provided alphabet in a for loop, and if an occurance of one of these upper or lower case letters was found in the 
# word passed into the function, add 1 to a count. Reducing the need to check if it had already been counted.
# def unique_english_letters(word):
#  uniques = 0
#  for letter in letters:
#    if letter in word:
#      uniques += 1
#  return uniques

# Since the provided alphabet string includes a single instance of all uppercase and lowercase letters in the English alphabet, 
# we can iterate through that string and see if our input strings contains the current letter we are looking at. 
# This can be accomplished using the keyword in. For every letter in the possible letters, we see if that letter is in our string!

# Write your count_char_x function here:
def count_char_x(word, x):
  counter = 0
  for letter in word:
    if letter == x:
      counter += 1
  return counter
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# This solution is similar to the last solution. In this case, we are looping through the input string and comparing it against the 
# input character. If they are the same, then we increase the counter

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  split_word = word.split(x)
  return (len(split_word)-1)
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
# In our function, we split the first input string using the second input string. What this does is cut the first string into an array
#  of smaller substrings containing the parts not equal to our second parameter x. For example, when splitting "mississippi" with the
#  string "iss", the resulting array will be [“m”, “”, “ippi”]. This includes the characters before "iss" was found, the empty space 
# between the two instances of "iss" and the characters after the last"iss". Be careful! In order to get the correct result we need to
#  return one less than the total number of split sections — in this example, "iss" was in the string twice, resulting in 3 sections.
# So we should return 3 - 1.

# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_in = word.find(start)
  end_in = word.find(end)
  if start_in != -1 and end_in != -1:
    return word[start_in+1:end_in]
  return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
# In this solution, we use the find function to get the starting and ending indices of our substring using our starting and ending
#  characters. After getting those, we check to make sure neither of them are -1. In order to extract the portion of the string within 
# those indices, we use slicing. We provide the starting index plus one in order to not include the starting character. 
# We do not need to provide the end index plus one, since the value on the right of the colon is excluded. 
# This causes our slicing to look like: word[start_ind+1:end_ind]).

# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split()
  for word in words:
    if len(word) < x:
      return False
    return True
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# We can use the split function with the space character provided in order to get an array of all of the words in the sentence. 
# Next, we use the in keyword in order to loop through every element in our array of words. We check the length of each word and compare
#  it against x to see if it is shorter. If any of the words in the array are shorter then we immediately return False and end the function.
# If we make through all of the words without returning False, we know we should return True since all of the word’s lengths were longer than x.