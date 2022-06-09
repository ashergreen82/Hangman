'''Hangman game
The exercise suggested that I use the "sowpods" list of over 200,000 scrabble words compiled by Peter Norvig.  So I did.
There are probably a dozen or so ways to do this, but I chose to reformat the word list by putting a number on each line
and then this made it easy to convert into a dictionary which I then made it easy to pick a random word by choosing a
random number.  I used this code to format the sowpods file to a new one called sowpods3:
for index, line in enumerate(wordlist):
    print("{} {}".format(index, line.strip()))
    with open("sowpods3.txt", "a") as sowpods:
        sowpods.write("{} {}".format(index, line.strip()))
        sowpods.write("\n")

So what the above code does is take each line and using the enumrate function I was able to assign an index to each line
and then write to the file, effectively giving me a list of words and their corresponding words.  Using the "with"
operator allows me to open and automatically close the file without having to worry about remembering to use the close()
function.

Requirements:
    Only let the user guess 6 times (head, body, 2 legs, and 2 arms), and tell the user how many guesses they have left.
    Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

Optional additions:

    When the player wins or loses, let them start a new game.
    Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!

'''

import random
from os import system, name

class WordListHandler:

    def __init__(self):
        self.word_array = []
        with open("sowpods.txt", "r") as self.word_list_source_file:
            for line in self.word_list_source_file:
                self.word_array.append(line.rstrip())
        # print(len(word_list))
        # print(type(self.word_array))

    def getRandomWord(self):
        self.random_word = random.choice(self.word_array)
        # length_of_word = len(self.random_word) - 1
        # for i in range(length_of_word):
        #     print("___" + " ", end="  ")

        return self.random_word

    def __str__(self):
        return f'The word is {self.random_word}'

class GamePlay:

    def __init__(self):
        self.random_word = WordListHandler()
        self.random_word.getRandomWord()
        self.clear()
        # print(self.random_word)

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def show_word_progress(self,guess_log_correct_responses):
        word_counter = 0
        length_of_word = len(self.random_word.random_word)
        for i in range(length_of_word):
            if self.random_word.random_word[i] in guess_log_correct_responses:
                print(self.random_word.random_word[i], end="  ")
                word_counter += 1
            else:
                print("___" + " ", end=" ")
        if word_counter == length_of_word:
            return True

    def check_to_see_if_player_has_won(self,guess_log_correct_responses):
        word_counter = 0
        length_of_word = len(self.random_word.random_word)
        for i in range(length_of_word):
            if self.random_word.random_word[i] in guess_log_correct_responses:
                word_counter += 1

    def display_noose(self):
        print('\n')
        print("   ------")
        print("  |      |")
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print("------------")

    def display_head(self):
        print('\n')
        print("   ------")
        print("  |      |")
        print('  |      O')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print("------------")

    def display_body(self):
        print('\n')
        print("   ------")
        print("  |      |")
        print('  |      O')
        print('  |      |')
        print('  |      |')
        print('  |')
        print('  |')
        print("------------")

    def display_left_hand(self):
        print('\n')
        print("   ------")
        print("  |      |")
        print('  |      O')
        print('  |      |')
        print('  |     /|')
        print('  |')
        print('  |')
        print("------------")

    def display_right_hand(self):
        print('\n')
        print("   ------")
        print("  |      |")
        print('  |      O')
        print('  |      |')
        print('  |     /|\\')
        print('  |')
        print('  |')
        print("------------")

    def display_left_leg(self):
        print('\n')
        print("   ------")
        print("  |      |")
        print('  |      O')
        print('  |      |')
        print('  |     /|\\')
        print('  |      |')
        print('  |      |')
        print('  |     /|')
        print('  |    / |')
        print('  |')
        print("------------")

    def display_right_leg(self):
        print('\n')
        print("   ------")
        print("  |      |")
        print('  |      O')
        print('  |      |')
        print('  |     /|\\')
        print('  |      |')
        print('  |      |')
        print('  |     /|\\')
        print('  |    / | \\')
        print('  |')
        print("------------")

    def end_of_game(self,game_on):
        player_decision = input("Would you like to play another round [type \"NO\" to end, or any key to continue]? ")
        if player_decision.upper() == "NO":
            game_on = False
        else:
            game_on = True
        return game_on

    def game_play(self):
        # body_parts = {1:"Head",2:"Body",3:"Left Arm",4:"Right Arm",5:"Left Leg",6:"Right Leg"}
        body_parts = ["Head", "Body", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]
        game_on = True
        guess_counter = 0
        number_of_guesses_wrong = 0
        number_of_guesses_right = 0
        guess_log = []
        guess_log_correct_responses = []
        while game_on:
            if guess_counter == 0:
                self.display_noose()
            if number_of_guesses_wrong == len(body_parts) + 1:
                self.display_right_leg()
                print(f"Well, you gave it your best shot!")
                print(f"The word was {self.random_word.random_word}.\nSorry, you lost the game.")
                game_on = self.end_of_game(game_on)
            else:
                has_the_player_won = self.show_word_progress(guess_log_correct_responses)
                if has_the_player_won is True:
                    print(f"\n\nCongratulations!  You have won the game with {guess_counter} guesses!\n")
                    game_on = self.end_of_game(game_on)
                    continue
                print (f"\n\nYou have made {guess_counter} guess(es) so far.")
                print(f"These are the letters you have already guessed: {guess_log}.")
                player_guess = input("Please enter your guess: ")
                if player_guess.upper() in self.random_word.random_word:
                    guess_counter += 1
                    guess_log.append(player_guess.upper())
                    guess_log_correct_responses.append(player_guess.upper())
                    number_of_guesses_right += 1
                else:
                    try:
                        print (f"Kiss your {body_parts[number_of_guesses_wrong]} goodbye")
                        number_of_guesses_wrong += 1
                        guess_counter += 1
                        guess_log.append(player_guess.upper())
                    except IndexError:
                        number_of_guesses_wrong += 1
                        guess_counter += 1
                        guess_log.append(player_guess.upper())
                self.clear()
                if number_of_guesses_wrong == 0:
                    self.display_noose()
                elif number_of_guesses_wrong == 1:
                    self.display_head()
                elif number_of_guesses_wrong == 2:
                    self.display_body()
                elif number_of_guesses_wrong == 3:
                    self.display_left_hand()
                elif number_of_guesses_wrong == 4:
                    self.display_right_hand()
                elif number_of_guesses_wrong == 5:
                    self.display_left_leg()
                elif number_of_guesses_wrong == 6:
                    self.display_right_leg()

    def __str__(self):
        # return f'player {self.name} has %s' % [str(x) for x in self.player_hand]
        pass

if __name__ == '__main__':

    play_hangman = GamePlay()
    play_hangman.game_play()
