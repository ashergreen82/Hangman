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
'''

#Step one is to open the file that contains a list of over 200000 words.

import random

class WordList:

    def __init__(self):
        self.word_list = []
        with open("sowpods.txt", "r") as word_list_source_file:
            for line in self.word_list:
                self.word_list.append(line)
        # print(len(word_list))
        print(type(self.word_list))

    def __str__(self):
        # return f'player {self.name} has %s' % [str(x) for x in self.player_hand]
        pass

class RandomWord:

    def __init__(self,word_list):
        self.random_word = random.choice(self.word_list)
        print(f"The random word is {self.random_word}")

    def create_word(self,word_list):
        pass

    def __str__(self):
        # return f'player {self.name} has %s' % [str(x) for x in self.player_hand]
        pass

class GamePlay:

    def __init__(self):
        self.word_list = WordList()
        # print(len(self.word_list))
        # self.random_word = RandomWord(self.word_list)
        word = RandomWord(self.word_list)
        word.create_word(self.word_list)

    def game_play(self):
        pass

    def __str__(self):
        # return f'player {self.name} has %s' % [str(x) for x in self.player_hand]
        pass

if __name__ == '__main__':
    play_hangman = GamePlay()
    play_hangman.game_play()
