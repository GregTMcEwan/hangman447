# Hangman Game

### Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

---

## Project Description

This project is a simple command-line **Hangman Game** implemented in Python. It allows the user to guess letters of a randomly chosen word from a predefined word list. The user has a limited number of lives, and the goal is to guess the word before running out of lives.

### Project Aim
- The aim of this project is to practice Python class structures, conditional logic, loops, and working with lists and strings.
- By building this project, I learned how to encapsulate game logic within a class, manage user input, and update game state efficiently.

### Features:
- Randomly selects a word from a word list.
- Allows the user to guess one letter at a time.
- Tracks user guesses and prevents duplicate guesses.
- Displays remaining lives after incorrect guesses.
- Displays the current state of the guessed word after each valid guess.

---

## Installation

To run this Hangman game on your local machine clone the repository and run the hangman.py file

**Ensure you have Python3 installed.**

---

## Usage

To start the game, simply run the hangman.py file
### Example Gameplay
```Gameplay
Please guess a letter: e
Good guess! e is in the word!
['_', '_', '_', '_', 'e']
Please guess a letter: r
Sorry, the letter r is not in the word. 
You have 4 lives left.
```
The game will continue until you either correctly guess the word, or run out of lives. 

---

## File Structure

tbd

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project, as long as you include the original copyright and license information.