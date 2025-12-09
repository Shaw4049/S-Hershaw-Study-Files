# Creating a turn based game for my Codecademy portfolio project

class Player:
    def __init__(self, input_name, health=100, attack_power=10):
        self.name = input_name
        self.health = health
        self.attack_power = attack_power
    
    def __repr__(self):
        return f"A Class Object to represent the player: {self.name}, Health: {self.health}, Attack Power: {self.attack_power}"
    
    def input_details(self):
        player_name = ""
        player_name = input("Welcome knight of the kingdom, what is your name? ")
        print("Welcome to the game Ser {player}!".format(player=player_name))

print(Player)