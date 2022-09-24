# Hangman Game
# Importing necessary modules

import random
import string
txt = ['python','list','hello','world','james','hero','project','program','windows','computer','tiger','java']
word = random.choice(txt).upper()
lives = len(word)
word_letters = set()        # set to have correct Letters in the word
used_letters = set()        # set of Letters player tried (correct or not)
print('The word is: ', '-' * len(word))
while lives > 0:
    wordprint = ''
    print(f'You have {lives}lives')
    letter = input('Enter the letter:-->').upper()
    if letter not in string.ascii_uppercase:
        print('Please provide Valid Input !!!:)')
    elif letter in used_letters:
        print('This letter already used..! Try Another letter')
    else:
        if letter not in word:
            print('Wrong letter!')          # For every wrong input - lives will be reduced by 1
            lives -= 1
        else:
            word_letters.add(letter)        # For correct input - lives won't get reduced
    used_letters.add(letter)
    for ch in word:                         # printing the word for every valid input
        if ch in word_letters:
            wordprint = wordprint + ''.join(ch)
        else:
            wordprint = wordprint + ''.join('-')
    print(wordprint)
    if wordprint == word:
        print('Congrats! You won!!')
        break
else:
    print('Sorry! You lost!\nThe word is:', word)
