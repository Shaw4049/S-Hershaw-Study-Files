# Declaring two lists to be utilised in the score dictionary.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Using zip comp to create a dictionary with the letters:points paired as key/value.
letters_to_points = dict(zip(letters, points))

# Iterating through the keys in the letter_to_points dict and adding lower case values.
for letter in list(letters_to_points.keys()):
    letters_to_points[letter.lower()] = letters_to_points[letter]

# Adding key for blank entry to equal zero.
letters_to_points[" "] = 0

print(letters_to_points)


# Defining a function to take the input word and total the score based on the points for each letter found in the letters_to_points dictionary.
def score_word(word):
    point_total = 0
    letters = list(word)
    for i in letters:
        if i in letters_to_points.keys():
            point_val = letters_to_points.get(i)
        else: 
            point_val = 0
        point_total += point_val
    return point_total

# Testing the function with a the word "BROWNIE", terminal should print 15.    
brownie_points = "BROWNie"
print(score_word(brownie_points))

# Creating a dictionary that maps players to a list of the words they have played, and an empty dictionary for players to points.
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

# Iterating through each players played words from player_to_words dict, and totalling the score of the words played. Then adding to the empty 
# dict along with the players name.
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)

# Defining a function to add a newly played word to the players played words (values) in the dict.
def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    player_to_words[player] = [word]

# Defining a function to use the play_word function to add a new played word, and returned updated total player score values.
def update_point_totals(name, played_word):
  play_word(name, played_word)
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points
      player_to_points[player] = sum(score_word(word) for word in player_to_words[player])
  return player_to_points

# player1 plays the word "automation", the score for this word is updated in the players_to_points dict.
update_point_totals("player1", "automation")
print(player_to_points)