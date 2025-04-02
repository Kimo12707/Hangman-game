# Name: Kamal Emadeldin

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    short_words = [word for word in wordlist ]
    return random.choice(short_words)
    

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def unique(str):
    count = ''
    for char in str:
        if char not in count:
            count += char
    return len(count)

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    prog = ''
    for letter in secret_word:
        if letter in letters_guessed:
            prog += letter
        else:
            prog += '*'    
    return prog        



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    remaining = ''
    for letter in string.ascii_lowercase:
        #a b c d e .....
        if letter not in letters_guessed:
            remaining += letter
    return remaining
   



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    num_of_guesses = 10
    letters_guessed = []
    print("Welcome to Hangman!")
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print("-----------------------------------------")  

    while num_of_guesses > 0:
        print(f'You have {num_of_guesses} guesses left')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guess = input('Please guess a letter: ')
        
        if not (guess.isalpha() and len(guess) == 1 or (with_help and guess == '!')):
            print("Oops! Invalid input. Enter a single letter or '!' for help.")
            print("-----------------------------------------")  
        if guess == '!':
            if with_help:
                if num_of_guesses >= 3:
                    choose_from = [letter for letter in secret_word if letter not in letters_guessed]
                    if choose_from:
                        revealed_letter = random.choice(choose_from)
                        letters_guessed.append(revealed_letter)
                        num_of_guesses -= 3
                        print(f'Letter revealed: {revealed_letter}')
                        print(f'{get_word_progress(secret_word, letters_guessed)}')
                        print("-----------------------------------------")
                        if get_word_progress(secret_word,letters_guessed) == secret_word:
                            print(f"Congratulations, you won! The word was: {secret_word}")
                            print(f"Your score: {(10 - num_of_guesses + 4 * unique(secret_word)) + (3 * len(secret_word))}")
                            play_again = input("Do you want to play again? Press 'r' to restart or any other key to exit: ")
                            if play_again.lower() == 'r':
                                new_secret_word = choose_word(wordlist)
                                hangman(new_secret_word, with_help)  # Restart the game with a new word

                            break
                    else:
                        print("No more letters to reveal!")
                else:
                    print("Not enough guesses left for help.")
                    print(f'{get_word_progress(secret_word, letters_guessed)}')
                    print("-----------------------------------------")
                continue  # Skip the remaining checks after help
        
        elif guess in letters_guessed:
            print("You've already guessed that letter.")
            print(f'{get_word_progress(secret_word, letters_guessed)}')
            print("-----------------------------------------")
            continue
        
        letters_guessed.append(guess)

        if guess in secret_word:
            print(f"Good guess! {get_word_progress(secret_word, letters_guessed)}")
            print("-----------------------------------------")
        else:
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
            print("-----------------------------------------")
            if guess in 'aeiou':
                num_of_guesses -= 2
            else:
                   num_of_guesses -= 1
        
        if has_player_won(secret_word, letters_guessed):
            print(f"Congratulations, you won! The word was: {secret_word}")
            print(f"Your score: {(10 - num_of_guesses + 4 * unique(secret_word)) + (3 * len(secret_word))}")
            play_again = input("Do you want to play again? Press 'r' to restart or any other key to exit: ")
            if play_again.lower() == 'r':
              new_secret_word = choose_word(wordlist)
              hangman(new_secret_word, with_help)  # Restart the game with a new word

            break  # End the game if player wins
    else:
        print(f"Sorry, you've run out of guesses. The word was: {secret_word}")
        play_again = input("Do you want to play again? Press 'r' to restart or any other key to exit: ")
        if play_again.lower() == 'r':
           new_secret_word = choose_word(wordlist)
           hangman(new_secret_word, with_help)  # Restart the game with a new word





if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

