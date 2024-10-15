import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.num_letters = int
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        print("Here")
        word=self.word.lower()
        guess = guess.lower() # Sets the user's guess and computer word to all lowercase for easier comparisons
        times_in_word = 0
        for char in word:
            if char==guess:
                times_in_word +=1
        if times_in_word > 0:
            print(f"Good guess! {guess} is in the word {times_in_word} times")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
        return 
    
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 or guess.isdigit() == True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            
        
game = Hangman(["Apple", "Pear", "Watermelon", "Strawberry"])
game.ask_for_input()