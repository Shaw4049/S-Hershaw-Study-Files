class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

rule_one = Rules()
print(rule_one.washing_brushes())
  

class Circle:
  pi = 3.14
  def area(self, radius):
    area = Circle.pi * radius ** 2
    return area

circle = Circle()
#Only the diameter was given, so halving the diameter to make the passed argument = the radius.
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area)


# Constructors
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    self.diameter = diameter
    print("New circle with diameter: " + str(self.diameter))

teaching_table = Circle(36)

# Instance Variables
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# Attribute Functions
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
  if hasattr(element, "count"):
      print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

# Self
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# Object Directory

print(dir(5))

def this_function_is_an_object():
  return

print(dir(this_function_is_an_object))

# String representation
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2

  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)