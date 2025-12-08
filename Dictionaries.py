# Defining two lists, one for song titles, one for play counts.
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Creating a dictionary with the key=songs and the value=playcounts via dict comprehension. Utilising the zip() method to combine the two lists
# into an iterator of tuples with the list elements paired together.
plays = {key:value for key, value in zip(songs,playcounts)}
print(plays)

# Adding the song "Purple Haze" and its associated playcount as a new key:value to the dictionary.
plays["Purple Haze"] = 1
# Ammending the playcount value of "Respect" in the existing dictionary.
plays["Respect"] = 94

# Creating a new library, the first key:value is a key of "Best" songs with the previous dictionary used as the value, whilst "Sunday Feelings"
# is a blank dictionary.
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)