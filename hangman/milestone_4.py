import random

class Hangman:
    """
    A class representing the Hangman game.
    
    Attributes:
    ----------
    word_list : list
        A list of words from which a random word is chosen for the game.
    word : str
        The word chosen randomly from word_list.
    word_guessed : list
        A list that stores the current state of the word with guessed letters.
    num_letters : int
        The number of unique letters remaining to guess.
    num_lives : int
        The number of lives the player has left.
    list_of_guesses : list
        A list to store the letters that the user has already guessed.
    """ 
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game with a word list and a number of lives.
        
        Parameters:
        ----------
        word_list : list
            The list of possible words for the game.
        num_lives : int
            The number of incorrect guesses the player is allowed. Default is 5.
        """
        self.word_list = word_list
        self.word = random.choice(word_list)  # Randomly select a word from the list
        self.word_guessed = []  # A list to hold guessed letters or blanks
        for c in self.word:
            self.word_guessed.append("_")  # Initially fill word_guessed with underscores
        self.num_letters = len(set(self.word))  # Count of unique letters to guess
        self.num_lives = num_lives  # Set the number of lives
        self.list_of_guesses = []  # To track the user's guesses

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.

        Parameters:
        ----------
        guess : str
            The letter guessed by the player.
        
        Returns:
        -------
        None
        """
        word = self.word.lower()  # Convert word to lowercase for comparison
        guess = guess.lower()  # Ensure guess is also lowercase        
        if guess in word:  # If the guess is correct
            print(f"Good guess! {guess} is in the word!")
            for i in range(len(word)): # Checks the word for the guessed letter
                if word[i] == guess:
                    self.word_guessed[i] = guess # adds the guessed letter's position in the secret word
            print(str(self.word_guessed)) 
            self.num_letters -= 1 # 
        else: # If the guess is incorrect
            self.num_lives -= 1 # Removes a life
            print(f"Sorry, {guess} is not in the word. \n You have {self.num_lives} lives left.") 
        return 
    
    def ask_for_input(self):
        """
        Continuously prompts the player to guess a letter until a valid guess is made.
        
        Returns:
        -------
        None
        """
        while True:
            guess = input("Please guess a letter: ")

            # Validate that the guess is a single alphabet character 
            if len(guess) != 1 or not guess.isalpha(): 
                print("Invalid letter. Please, enter a single alphabetical character.")

            # Prevents the user from guessing the same character twice
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            
            # Processes a valid guess
            else:
                self.check_guess(guess) # Calls check_guess to handle the guessed letter
                self.list_of_guesses.append(guess) # Adds guess to list of guessed letters
            
        
game = Hangman(["Apple", "Pear", "Watermelon", "Strawberry"])
game.ask_for_input()