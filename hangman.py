import random
from textwrap import wrap

def is_there(word, yourword, letter):
        for i in range(0, len(word)):
            c = word[i]
            if c == letter:
                yourword[i] = c
                return 0;
        return -1;
# display game name
print('''

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝                      
''')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# where are the words?
words = ('ant baboon badger bat bear beaver camel cat clam cobra').split()

# 64 words, get a single word
word = words[random.randint(0, len(words) - 1)]

print(word)
# generate spaces 
guessed_word = ['_'] * len(word)
 

count = 0;
word_count = 0;
while count != 7:
    c = input("Guess the word: ")
    if word_count + 1 == len(word):
        print(guessed_word_str)
        print("you won")
        break;
    if is_there(word, guessed_word, c) == 0:
        word_count+=1;
        guessed_word_str = ''.join(guessed_word)
        print(guessed_word_str)
    else:
        print(HANGMANPICS[count])
        count+=1

if count == 7:
    print("you lose")
    

    