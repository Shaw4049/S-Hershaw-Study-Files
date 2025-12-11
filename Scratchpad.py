letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
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

# You can start with the
# Cat class or erase this
# and use your own!
class Cat:
  def __init__(self, input_name, input_breed, input_age = 0, input_is_cuddly = True, input_gender = "Female"):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_cuddly = input_is_cuddly
    self.gender = input_gender
  
  # Create method to change
  # at least one attribute.
  # Ex: def change_att(self):
  def is_asshole(self, assholishness):
    if assholishness > 5:
      self.is_cuddly = False
      print("Your cat is an asshole and not cuddly.")
    else:
      print("Your cat isn't too bad")
    return self.is_cuddly
  def can_breed_with(self, other_cat):
    if self.gender != other_cat.gender:
      print("These cats can breed.")
      return True
    else:
      print("These cats cannot breed.")
      return False  

# Create two pets.
cat_one = Cat("Leo", "Tabby", 3, False, "Male")
cat_two = Cat("Luna", "Siamese", 2, True, "Female")

# Test your method
cat_one.can_breed_with(cat_two)

# Call your method on your
# new pet here.
cat_one.is_asshole(4)

class Dog:
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness=True):
    # Dog attributes...
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.is_friendly = input_friendliness
        self.friends = []

  # self will equal this specific dog
  # other_dog will be an argument we pass in
  def become_friends(self, other_dog):
    if(other_dog.is_friendly):
      # If the other dog is friendly,
      # it adds other_dog to its friends
      self.friends.append(other_dog)
      # The other dog also adds this 
      # specific dog to its friends
      other_dog.friends.append(self)
      print("{name} become friends with {other_name}!".format(name = self.name, other_name = other_dog.name))
    else:
      # If the other dog is NOT friendly,
      # no one becomes friends.
      print("{other_name} did not want to become friends with {name}!".format(name = self.name, other_name = other_dog.name))
dog_one = Dog("Sparky", "Golden Retriever", 5, True)
dog_two = Dog("Bruno", "Chihuahua", 10, False)

# When Sparky asks Bruno, Bruno says no.
dog_one.become_friends(dog_two)
# Output: "Bruno did not want to become friends with Sparky!"

# When Bruno asks Sparky, Sparky says yes!
dog_two.become_friends(dog_one)
# Output: "Bruno became friends with Sparky!"

