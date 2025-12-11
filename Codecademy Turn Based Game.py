# Creating a turn based game for my Codecademy portfolio project
# Fight Night

class Player:
    def __init__(self, input_name, health=100, attack_power=10, defense=10, stat_points= 30):
        self.name = input_name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.stat_points = stat_points
    
    def __repr__(self):
        return f"A Class Object to represent the player: {self.name}, Health: {self.health}, Attack Power: {self.attack_power}, Defense: {self.defense}."
    
    def input_details(self):
        player_name = ""
        player_name = input("Welcome fighter, what is your name? ")
        print("Welcome to the game {player}!".format(player=player_name))
        print("Your starting health is {health}, your attack power is {attack} and your defense rating is {defense}.".format(health=self.health, attack=self.attack_power, defense = self.defense))
        print("You have an additional {points} points to spend on your three stats." .format(points=self.stat_points))
    # User input to allocate additional points to health.
    def input_health_stats(self):
        health_add = 0
        while True:
            # Prompt and validate integer input.
            try:
                health_add = int(input("How many points would you like to add to your health? "))
            except ValueError:
                print('Please enter a valid number.')
                continue

            if health_add < 0:
                print('Your number cannot be negative.')
                continue
            if health_add > self.stat_points:
                print("You do not have enough points to allocate that many to health.")
                continue

            # Valid value: apply and exit loop
            self.health += health_add
            self.stat_points -= health_add
            print("Your health is now {health}, you have {points} remaining. ".format(health=self.health, points=self.stat_points))
            break
        return
    # User input to allocate additional points to attack power.
    def input_attack_stats(self):
        attack_add = 0   
        while True:
            # Prompt and validate integer input.
            try:
                attack_add = int(input("How many points would you like to add to your attack power? "))
            except ValueError:
                print('Please enter a valid number.')
                continue
            if attack_add < 0:
                print('Your number cannot be negative.')
                continue
            elif attack_add > self.stat_points:
                print("You do not have enough points to allocate that many to your attack rating.")
                continue
            # Valid value: apply and exit loop
            self.attack_power += attack_add
            self.stat_points -= attack_add
            print("Your attack rating is now is now {attack}, you have {points} remaining. ".format(attack=self.attack_power, points=self.stat_points))
            break
        return
    # User input to allocate additional points to defense.
    def input_defense_stats(self):
        defense_add = 0
        while True:
            # Prompt and validate integer input.
            try:
                defense_add = int(input("How many points would you like to add to your defense rating? "))
            except ValueError:
                print('Please enter a valid number.')
                continue    
            if defense_add < 0:
                print('Your number cannot be negative.')
                continue
            elif defense_add > self.stat_points:
                print("You do not have enough points to allocate that many to your attack rating.")
                continue
            # Valid value: apply and exit loop
            self.defense += defense_add
            self.stat_points -= defense_add
            print("Your defense rating is now is now {defense}, you have {points} remaining. ".format(defense=self.attack_power, points=self.stat_points))
            break
        return
    
    def list_stats(self):
        print("Player Name: {name}. You have entered the following stats: \nHealth: {health}\nAttack Power: {attack}\nDefense: {defense}\n".format(name=self.name, health=self.health, attack=self.attack_power, defense=self.defense))
        return

# Create a player object and run through the stat allocation process.
player_one = Player("Player One")
player_one.input_details()
player_one.input_health_stats()
player_one.input_attack_stats()
player_one.input_defense_stats()
player_one.list_stats()
