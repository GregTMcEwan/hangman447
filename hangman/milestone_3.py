import random

word_list =["Apple", "Bannana", "Strawberry", "Pear", "Dragonfruit"]
print(word_list)
word = random.choice(word_list)
print(word)

def get_user_guess(): # Function that prompts the user to input a guess, validates it is a single non number character and returns it
    while True:
        guess = input("Input your guess: ")
        if len(guess) == 1 and guess.isdigit() == False:
            print("Valid guess!")
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

user_guess = get_user_guess()
def check_user_guess(word, user_guess): ## Checks how many times the users guess appears in the secret word
    word=word.lower()
    user_guess = user_guess.lower() # Sets the user's guess and computer word to all lowercase for easier comparisons
    times_in_word = 0
    for char in word:
        if char==user_guess:
            times_in_word +=1
    if times_in_word > 0:
        print(f"Good guess! {user_guess} is in the word {times_in_word} times")
    else:
        print(f"Sorry, {user_guess} is not in the word. Try again.")
    return 


check_user_guess(word ,user_guess)


