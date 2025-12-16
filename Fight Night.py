# Creating a turn based game for my Codecademy portfolio project
import random

class Player:
    def __init__(self, input_name, health=100, attack_power=25, defense=10, stat_points= 30):
        self.name = input_name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.stat_points = stat_points
    
    def __repr__(self):
        return f"A Class Object to represent the player: {self.name}, Health: {self.health}, Attack Power: {self.attack_power}, Defense: {self.defense}."
    
    # User input to get player name and display starting stats.
    def input_details(self):
        player_name = ""
        player_name = input("Welcome {player_number}, what is your name? ".format(player_number=self.name))
        print("Welcome to the game {player}!".format(player=player_name))
        print("Your starting health is {health}, your attack power is {attack} and your defense rating is {defense}.".format(health=self.health, attack=self.attack_power, defense = self.defense))
        print("You have an additional {points} points to spend on your three stats." .format(points=self.stat_points))
        self.name = player_name
    # User input to allocate additional points to health.
    def input_health_stats(self):
        health_add = 0
        while True:
            # Prompt and validate integer input.
            try:
                health_add = int(input("How many points would you like to add to your health? From the {points} points available. ".format(points=self.stat_points)))
            except ValueError:
                print('Please enter a whole valid number.')
                continue

            if health_add < 0:
                print('Your number cannot be negative. Pease enter a whole valid number.')
                continue
            if health_add > self.stat_points:
                print("You do not have enough points to allocate that many to health. You only have {points} remaining. ".format(points=self.stat_points))
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
                attack_add = int(input("How many points would you like to add to your attack power? From the {points} points available. ".format(points=self.stat_points)))
            except ValueError:
            
                print('Please enter a valid number.')
                continue
            if attack_add < 0:
                print('Your number cannot be negative. Please enter a whole valid number.')
                continue
            elif attack_add > self.stat_points:
                print("You do not have enough points to allocate that many to your attack rating.You only have {points} remaining. ".format(points=self.stat_points))
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
                defense_add = int(input("How many points would you like to add to your defense rating? From the {points} points available. ".format(points=self.stat_points)))
            except ValueError:
                print('Please enter a valid number.')
                continue    
            if defense_add < 0:
                print('Your number cannot be negative. Please enter a whole valid number.')
                continue
            elif defense_add > self.stat_points:
                print("You do not have enough points to allocate that many to your attack rating. You only have {points} remaining. ".format(points=self.stat_points))
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


# Creating a Fight class to manage and automate the fight between two players.
class Fight:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
    
    def __repr__(self):
        return f"A Class Object to represent the fight between {self.player_one.name} and {self.player_two.name}."
    
    def battle(self):
        print("Let the fight begin!")
        round = 1
        while self.player_one.health > 0 and self.player_two.health > 0:
            print("Round {round}!".format(round=round))
            if first_move == 1:
                damage = self.player_one.attack_power - self.player_two.defense
                self.player_two.health -= damage
                if damage < 0:
                    damage = 0
                print("{attacker} attacks {defender} for {damage} damage! {defender} has {health} health remaining.".format(attacker=self.player_one.name, defender=self.player_two.name, damage=damage, health=self.player_two.health))
                if self.player_two.health <= 0:
                    print("{defender} has been defeated! {attacker} wins!".format(defender=self.player_two.name, attacker=self.player_one.name))
                    break
                damage = self.player_two.attack_power - self.player_one.defense
                self.player_one.health -= damage
                if damage < 0:
                    damage = 0
                print("{attacker} attacks {defender} for {damage} damage! {defender} has {health} health remaining.".format(attacker=self.player_two.name, defender=self.player_one.name, damage=damage, health=self.player_one.health))
                if self.player_one.health <= 0:
                    print("{defender} has been defeated! {attacker} wins!".format(defender=self.player_one.name, attacker=self.player_two.name))
                    break
            else:
                damage = self.player_two.attack_power - self.player_one.defense
                self.player_one.health -= damage
                if damage < 0:
                    damage = 0
                print("{attacker} attacks {defender} for {damage} damage! {defender} has {health} health remaining.".format(attacker=self.player_two.name, defender=self.player_one.name, damage=damage, health=self.player_one.health))
                if self.player_one.health <= 0:
                    print("{defender} has been defeated! {attacker} wins!".format(defender=self.player_one.name, attacker=self.player_two.name))
                    break
                damage = self.player_one.attack_power - self.player_two.defense
                self.player_two.health -= damage
                if damage < 0:
                    damage = 0
                print("{attacker} attacks {defender} for {damage} damage! {defender} has {health} health remaining.".format(attacker=self.player_one.name, defender=self.player_two.name, damage=damage, health=self.player_two.health))
                if self.player_two.health <= 0:
                    print("{defender} has been defeated! {attacker} wins!".format(defender=self.player_two.name, attacker=self.player_one.name))
                    break
            round += 1
        return
 
# Determine who goes first with a random number generator.
first_move = random.randint(1,2)
# Fight Night
print("Welcome to Fight Night! Get ready to rumble!")

# Create a player object and run through the stat allocation process.
player_one = Player("Player One")
player_one.input_details()
player_one.input_health_stats()
player_one.input_attack_stats()
player_one.input_defense_stats()
player_one.list_stats()

# Create a second player object and run through the stat allocation process.
player_two = Player("Player Two")
player_two.input_details()
player_two.input_health_stats()
player_two.input_attack_stats()
player_two.input_defense_stats()
player_two.list_stats()

# Create a Fight object and start the battle.
fight_night = Fight(player_one, player_two) 
fight_night.battle()