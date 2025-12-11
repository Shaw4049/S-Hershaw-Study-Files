# Every Third Number
#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))
#Uncomment the line below when your function is done
print(every_three_nums(91))

# We can write the body of this function in one line by nesting the range() function inside of the list() function. 
# The range function accepts the starting number, the ending number (exclusive), and the amount to increment by. 

# Remove Middle
#Write your function here
def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# This can be solved using one line of code if you combine and slice the lists at the same time. Slicing allows us to get the segments of the list before and after the index range 
# and the operation + allows us to combine them together.

# More Frequent Item
#Write your function here
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# We use the count() function to find the number of occurrences for each item. We then compare the counts against each other to find the item which appears the most in the list. 
# The item with the most appearances is returned by the function.

# Double Index
#Write your function here
def double_index(my_list, index):
  # Checks to see if index is too big
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list 
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

# Note that this solution is careful not to modify the original input list. If we were to simply use my_list[index] = my_list[index] * 2 then the list that was passed into the function would 
# be modified outside of the function as well. Creating a new list and writing the values to it prevents this from happening. We use slicing to extract the values before and after the index 
# and we append the modified value at the index to our new list. 

# Middle Item
#Write your function here
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2
  else:
    return my_list[int(len(my_list)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

# We used modulus to determine if the list had an even or odd number of elements. After determining this, for an odd number of elements, we calculate the middle index and return the middle 
# element from the list. For an even number of elements, we calculate the index of the element close to the middle and the other element close to the middle (by subtracting 1 from the middle calculation). 
# We get the values at those indices and calculate the average.
# Note that the math to find the middle index is a bit tricky. In some cases, when we divide by 2, we would get a double. For example, if our list had 3 items in it, 
# then 3/2 would give us 1.5. The middle index should be 1, so in order to go from 1.5 to 1, we cast 1.5 as an int. In total, this is int(len(my_list)/2).
