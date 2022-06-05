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

class WordListHandler:

    def __init__(self):
        self.word_array = []
        with open("sowpods.txt", "r") as self.word_list_source_file:
            for line in self.word_list_source_file:
                self.word_array.append(line)
        # print(len(word_list))
        print(type(self.word_array))

    def getRandomWord(self):
        self.random_word = random.choice(self.word_array)
        return self.random_word

    def __str__(self):
        return f'The word is {self.random_word}'

class GamePlay:

    def __init__(self):
        self.random_word = WordListHandler()
        self.random_word.getRandomWord()
        print(self.random_word)

    def show_word_progress(self,guess_log_correct_responses):
        for i in range(len(self.random_word.random_word)):
            for j in guess_log_correct_responses:
                if j in self.random_word.random_word:
                    print(guess_log_correct_responses[i])
                else:
                    print("_____"+" ")

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
            if number_of_guesses_wrong == 6:
                print(f"The word was {self.random_word.random_word}.\nSorry, you lost the game.")
                game_on = False
            else:
                self.show_word_progress(guess_log_correct_responses)
                print (f"You have made {guess_counter} guess(es) so far.")
                print(f"These are the letters you have already guessed: {guess_log}.")
                player_guess = input("Please enter your guess: ")
                if player_guess.upper() in self.random_word.random_word:
                    print("Correct")
                    guess_counter += 1
                    guess_log.append(player_guess.upper())
                    guess_log_correct_responses.append(player_guess.upper())
                    number_of_guesses_right += 1
                else:
                    print (f"Kiss your {body_parts[number_of_guesses_wrong]} goodbye")
                    number_of_guesses_wrong += 1
                    guess_counter += 1
                    guess_log.append(player_guess.upper())

    def __str__(self):
        # return f'player {self.name} has %s' % [str(x) for x in self.player_hand]
        pass

if __name__ == '__main__':

    play_hangman = GamePlay()
    play_hangman.game_play()
