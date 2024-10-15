import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = []
        for c in self.word:
           self.word_guessed.append("_")
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        word=self.word.lower()
        guess = guess.lower() # Sets the user's guess and computer word to all lowercase for easier comparisons
        if guess in word:
            print(f"Good guess! {guess} is in the word!")
            for i in range(len(word)):
                if word[i]==guess:
                    self.word_guessed[i]=guess
                    print(str(self.word_guessed))
            self.num_letters -= 1
            print(self.num_letters)
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. \n You have {self.num_lives} lives left.")
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