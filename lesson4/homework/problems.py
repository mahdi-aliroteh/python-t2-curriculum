# Problem 1
# Ask the user for a sentence.
# Use a dictionary to count how many times each word appears.
# Print the dictionary.
# (Hint: split the sentence)
input_sent = input('Please enter a sentence: ')
sent = str(input_sent)
word_count = {}

for word in sent.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for count in word_count.values():
    count = count + 1
print(word_count)
print(count - 1)
# Problem 2
# Create a dictionary called capitals with states and their capitals.
# Ask the user for a state and print the capital.
# If not found, print "No data".
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}
input_state = input('Please enter the name of a state to find its capital: ')
state = str(input_state)
if state in capitals:
    print(capitals[state])
else:
    print("No Data")

# Problem 3
# Ask the user for a word.
# Print the letter that appears the most times.
# If there is a tie, print any one of them.
input_word = input('Please enter a word: ')
word = str(input_word)
letter_count = {}

for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

most_used = max(letter_count, key=letter_count.get)
print(most_used)
    

# Problem 4
# Create a dictionary called inventory with items and their quantity.
# Ask the user what item they want to buy and how many.
# If there are enough, subtract from the inventory and print the new inventory.
# Otherwise print "Not enough".
items = {
    'sword':6,
    'gem':4,
    'medkit':2
}
input_item = input('Which item would you want. The sword, gem, or the medkit: ')
item = str(input_item)
input_amount = input('How many do you want: ')
amount = int(input_amount)
if item in items:
    availableAmount = items[item]
    if availableAmount >= amount:
        item[items] = availableAmount - amount
    else:
        print("Not enough")
else:
    print("Invalid item")
print(items)

# Problem 5
# Ask the user for two words.
# Use dictionaries to check if they are anagrams (same letters, different order).
# Print "Anagram" or "Not anagram".
# Ask the user for two words
word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()

dict1 = {}
dict2 = {}
for letter in word1:
    if letter in dict1:
        dict1[letter] += 1
    else:
        dict1[letter] = 1

for letter in word2:
    if letter in dict2:
        dict2[letter] += 1
    else:
        dict2[letter] = 1

if dict1 == dict2:
    print("Anagram")
else:
    print("Not anagram")
