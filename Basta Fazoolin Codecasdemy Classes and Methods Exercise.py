

# Creating a new class to accomodate the new business the company is expanding into.
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Creating a Franchise class, with a constructor taking in an adress, list of menus and a name for the franchised resturant.
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  # # Adding representation that returns the address of the franchised restuant.
  def __repr__(self):
    return self.address
  # Adding a method to the class to take in a given time, then look through the .menus object, examining for each if the givem time is after the start time and before the end time of each menus, 
  # then if so appending the emply list of available_menus, with the determined available menu.
  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

# Creating a Menu class, with a constructor to handle five parameters, menu name, menu items, menu start time, menu end time.
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # Adding representation that returns a concatinated string detailing the menu name and times it is available from.
  def __repr__(self):
    return self.name + ' menu available from ' +str(self.start_time) + ' until ' +str(self.end_time)
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

# Dictionary holding the brunch menu items.
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
# Creating the brunch menu object and passing in the required parameters.
brunch_menu = Menu("Brunch",brunch_items , 1100, 1600)
# Dictionary holding the early bird menu items
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
# Creating the early bird menu object and passing in the required parameters.
early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)
# Dictionary holding the brunch menu items.
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

# Creating the dinner menu object and passing in the required parameters.
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)
# Dictionary holding the kids menu items.
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
# Creating the kids menu object and passing in the required parameters.
kids_menu = Menu("Kids", kids_items, 1100, 2100)

# Testing string representation
#print(brunch_menu)
# Testing calcualte bill, brunch should print 13.50
# print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
# Testing calcualte bill, early bird should print 21.50
# print(early_bird_menu.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

# Creating the franchise objects passing in arguments for resturant address and a list of available menus.
flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

# Testing the representation of the Franchise class. 
#print(flagship_store)
# Testing the output of the available menus method of the franchise class with 1200 and 1700 as passed arguments.
#print(flagship_store.available_menus(1200))
#print(flagship_store.available_menus(1700))

# Creating an object of the Business class for the existing business' and their two locations.
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
# Creating a dictionary holding the menu items of the new arepas business.
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
# Creating the Arepas menu object and passing in the required parameters.
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)
# Calling the Franchise class to create a new object for the Take a' Arepa business.
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
# Calling the Business class to create a new object for the Take a' Arepa business.
arepa = Business("Take a' Arepa", [arepas_place])

# Testing calling the menus available for the new business.
print(arepa.franchises[0].menus[0])
