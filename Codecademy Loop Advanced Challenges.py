# Larger Sum 
#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# In this solution, we manually iterate through each element in each list and calculate our sums. We then return the list with the greater sum and break the tie by returning lst1. 
# You can also try solving this problem using the sum() function in python. The body of this function could also be condensed into one line of code if you want an additional challenge!

# Over 9000
#Write your function here
def over_nine_thousand(lst):
  sum = 0 
  for number in lst:
    sum += number
    if sum > 9000:
        break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# Our solution follows a similar pattern to some of the other code challenges, except that we have a condition where we end early. In the case where we reach a sum greater than 9000, we can use the break keyword to exit our loop. 
# This will continue to execute the code outside of our loop, which in this case, returns the sum that we found.

# Max Num
#Write your function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# There are a few different ways to accomplish this task, but the way we did it was to check every element in the list and see if there is one bigger than what we currently think is the biggest. 
# If there is a bigger one, then replace it. We keep replacing the number until the largest number has been found.

# Same Values
#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# In this solution, we used a loop that iterates using the range of the len of our list. This generates the indices we need to iterate through. Note that we assume the lists are of equal size. 
# We then access the element at the current index from each list using lst1[index] and lst2[index]. If they are equal we add the index to the new list. Finally, we return the results. 

# Reversed List
#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst1) - 1 - index]:
      return False
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# In this code, we iterate through each of the indices for the entire length of either of the lists (since we assume the lengths are equal) and we perform a comparison on each of the elements. 
# We get the element at the current index from our first list with lst1[index] and we test it against the last index of the second list minus the current index len(lst2) - 1 – index.
# That math is a little complicated — it helps to look at a concrete example. If we are given a list of 5 elements, the valid indices are 0 to 4. 
# Because of this, the last index in the second list is len(lst2) - 1, or 5 - 1 = 4. Now in order to get the inverse of the position we are at in the first list, we subtract the index we are at from the 
# end of the second list. So on the first pass, we’ll compare the element at position 0 to the element at position 5 - 1 - 0 = 4. On the next pass, we’ll compare the element at position 1 to the element at 
# position 5 - 1 - 1 = 3, and so on.
# If any of the two elements are not equal then we know that the second list is not the reverse of the first list and we return False. 
# If we made it to the end without a mismatch then we can return True since the second list is the reverse of the first. 
# You could also try simplifying this code by using the python function reversed() or other methods that you will learn later on such as ‘slicing’.