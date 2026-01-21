# Problem 1
# Ask the user for a word.
# Print the word reversed using slicing.
user_input=input("Please enter a word: ")
user = str(user_input)
print(user[::-1])

# Problem 2
# Ask the user for a word and a letter.
# Print how many times the letter appears in the word (case-insensitive).
input_word=input('Please enter a word: ')
input_letter=input('Please enter a letter: ')
word = str(input_word)
letter = str(input_letter)
count = 0
for x in range(len(word)):
    if letter == word[x]:
        count = count + 1
print(f'Your letter appeared {count} times in the word {word}')

# Problem 3
# Ask the user for an email address like "name@example.com".
# Print only the part after the @ (example: "example.com").
input_email = input('Please enter your email: ')
email = str(input_email)
num = email.index('@')
print(email[num + 1:])


# Problem 4
# Ask the user for a word.
# Print the word without the first and last character.
input_word=input('Please enter a word: ')
word = str(input_word)
print(word[1:len(word) - 1])

# Problem 5
# Ask the user for a sentence.
# Print "Long" if the sentence has more than 20 characters (including spaces),
# otherwise print "Short".
input_word=input('Please enter a word: ')
word = str(input_word)
if len(word) > 20:
    print('Long')
else:
    print('Short')