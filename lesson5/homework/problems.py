# Problem 1
# Create a class called BankAccount.
# __init__ takes owner and balance.
# Make a method deposit(amount) that adds to balance.
# Make a method withdraw(amount) that subtracts only if there is enough money.
# Test it with a few deposits and withdrawals.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f'New balance is: ${self.balance:.2f}')
    def withdraw(self, amount):
        if self.balance >= self.amount:
            self.balance -= amount
            print(f'New balance is: ${self.balance:.2f}')
input_name = input('Enter the owner name to create account: ')
name = str(input_name)
input_balance = input('Enter initial account balance: ')
balance = float(input_balance)
account = BankAccount(name, balance)
input_act = input('Would you like to deposit or withdraw: ')
act = str(input_act)
input_amount = input('How much: ')
amount = float(input_amount)

if act == 'deposit':
    account.deposit(amount)
elif act == 'withdraw':
    account.withdraw(amount)
else:
    print('invalid action')

# Problem 2
# Create a class called Car.
# __init__ takes model and miles.
# Make a method drive(distance) that adds to miles.
# Create a Car and drive it a few times, printing miles each time.
class Car:
    def __init__(self, model, miles):
        self.model = model
        self.miles = miles
    def drive(self, distance):
        self.miles += distance
        print(f'New milage is {self.miles}')
input_model = input('Please enter the model of your car: ')
model = str(input_model)
input_milage = input('What is initial milage: ')
milage = int(input_milage)
car = Car(model, milage)
for i in range(3):
    input_drive = input('What ditance do you want to drive it: ')
    drive_miles = int(input_drive)
    car.drive(drive_miles)


# Problem 3
# Create a class called ScoreKeeper.
# It stores a dictionary of player scores.
# Make a method add_points(name, points) that adds points for that player.
# Print the final dictionary after adding points for a few players.
class ScoreKeeper:
    def __init__(self):
        self.playerScores = {}
    def add_points(self, name, points):
        self.playerScores[name] = self.playerScores.get(name, 0) + points
score_keeper = ScoreKeeper()
for i in range(3):
    input_name = input('Enter a player name: ')
    name = str(input_name)
    input_points = input('Enter point amount for this player: ')
    points = int(input_points)
    score_keeper.add_points(name, points)
print('Final scores are:')
print(score_keeper.playerScores)

# Problem 4
# Create a class called Timer.
# It starts at 0 seconds.
# Make a method tick() that adds 1.
# Make a method reset() that sets it back to 0.
# Test tick() and reset().
class Timer:
    def __init__(self):
        self.seconds = 0
    def tick(self):
        self.seconds += 1
    def reset(self):
        self.seconds = 0
timer = Timer()
for i in range(10):
    timer.tick()
    print(f'Time is at {timer.seconds} seconds.')
timer.reset()
print(f'After reset time is at {timer.seconds} seconds.')

# Problem 5
# Create a class called WordTracker.
# It stores a word (string).
# Make a method add_letter(letter) that adds the letter to the end.
# Make a method remove_last() that removes the last letter (if it exists).
# Test it.
class WordTracker:
    def __init__(self):
        self.word = ""
    def add_letter(self, letter):
        self.word += str(letter)
    def remove_last(self):
        self.word = self.word[:-1]
word_tracker = WordTracker()
for i in range(4):
    input_letter = input('Enter a letter:')
    word_tracker.add_letter(input_letter)
print(f'You created a 4-letter word: {word_tracker.word}')
word_tracker.remove_last()
word_tracker.remove_last()
print(f'Your word after removing last 2 letters: {word_tracker.word}')