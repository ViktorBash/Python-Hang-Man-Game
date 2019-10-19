import random
import re


hidden_word = ""
number = random.randint(0, 6)

if number == 0:
    hidden_word = "christmas"
elif number == 1:
    hidden_word = "flowers"
elif number == 2:
    hidden_word = "scrumptious"
elif number == 3:
    hidden_word = "terrorizing"
elif number == 4:
    hidden_word = "inquisitive"
elif number == 5:
    hidden_word = "treasure"
elif number == 6:
    hidden_word = "gold"

spaces = ["_"]
for i in range(0, (len(hidden_word)-1)):
    spaces.append("_")
print(' '.join(spaces))

unused_letters = ""
solved = False
number_of_guesses = 0


while solved is False:
    print("Welcome to hangman! Try and guess the word in as little guesses as possible ")
    print("Current amount of guesses: " + str(number_of_guesses))
    print("")
    print(' '.join(spaces))
    print("Unused letters: " + unused_letters)
    print("")
    print("To guess, enter a lowercase letter.")
    user_guess = str(input(""))
    number_of_guesses = number_of_guesses + 1
    if user_guess in hidden_word:
        instances = []
        instances = [m.start() for m in re.finditer(user_guess, hidden_word)]
        for i in range(0, len(instances)):
            spaces[instances[i]] = user_guess
        # position = hidden_word.find(user_guess) Old way of finding position, only returned lowest position
        # spaces[position] = user_guess
        print(' '.join(spaces))
        if "_" not in spaces:
            solved = True
    elif user_guess not in hidden_word:
        if user_guess in unused_letters:
            print("You already guessed this letter")
        else:
            unused_letters = (unused_letters + " " + user_guess)
print("Congratulations! You finished the hangman game with " + str(number_of_guesses) + " guesses! Good job")
