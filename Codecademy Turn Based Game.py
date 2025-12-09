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
        health_add = 0
        attack_add = 0
        defense_add = 0
        player_name = ""
        player_name = input("Welcome fighter, what is your name? ")
        print("Welcome to the game {player}!".format(player=player_name))
        print("Your starting health is {health}, your attack power is {attack} and your defense rating is {defense}.".format(health=self.health, attack=self.attack_power, defense = self.defense))
        print("You have an additional {points} points to spend on your three stats." .format(points=self.stat_points))
    # User input to allocate additional points to health.
    def input_health_stats(self):
        health_add = 0
        while health_add == 0 :
            # User input to allocate additional points to health, attack power, and defense
            # Health allocation
            health_add = int(input("How many points would you like to add to your health? "))
            if health_add != int:
                print('Please enter a valid number.')
                health_add = 0
                continue
            elif health_add < 0:
                print('Your number cannot be negative.')
                health_add = 0
                continue
            elif health_add > self.stat_points:
                print("You do not have enough points to allocate that many to health.")
                health_add = 0
                continue
            elif health_add == 0 or health_add >0:
                self.health += health_add
                self.stat_points -= health_add
                print("Your health is now {health}, you have {points} remaining. ".format(health=self.health, points=self.stat_points))
        return    
    # User input to allocate additional points to attack power.
    def input_attack_stats(self):
        attack_add = 0   
        while attack_add == 0 :
            attack_add = int(input("How many points would you like to add to your attack power? "))
            if attack_add < 0:
                print('Your number cannopt be negative.')
                continue
            elif attack_add > self.stat_points:
                print("You do not have enough points to allocate that many to your attack rating.")
                continue
            elif attack_add == 0 or attack_add >0:
                self.attack_power += attack_add
                self.stat_points -= attack_add
                print("Your attack rating is now is now {attack}, you have {points} remaining. ".format(attack=self.attack_power, points=self.stat_points))
        return
    # User input to allocate additional points to defense.
    def input_defense_stats(self):
        defense_add = 0
        while defense_add == 0 :
            defense_add = int(input("How many points would you like to add to your defense rating? "))
            if defense_add < 0:
                print('Your number cannopt be negative.')
                continue
            elif defense_add > self.stat_points:
                print("You do not have enough points to allocate that many to your attack rating.")
                continue
            elif defense_add == 0 or defense_add >0:
                self.defense += defense_add
                self.stat_points -= defense_add
                print("Your defense rating is now is now {defense}, you have {points} remaining. ".format(defense=self.attack_power, points=self.stat_points))
        return

player_one = Player("Player One")
player_one.input_details()
player_one.input_health_stats()
player_one.input_attack_stats()
player_one.input_defense_stats()
