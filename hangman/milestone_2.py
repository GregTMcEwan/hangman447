import random

word_list =["Apple", "Bannana", "Strawberry", "Pear", "Dragonfruit"]
print(word_list)
word = random.choice(word_list)
print(word)

def get_user_guess(): # Function that prompts the user to input a guess, validates it is a single non number character and returns it
    while True:
        guess = input("Input your guess: ")
        if len(guess) == 1 and guess.isdigit() == False:
            print("Good guess!")
            return guess
        else:
            print("Oops! That is not a valid input.")

guess = get_user_guess()