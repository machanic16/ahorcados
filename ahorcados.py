# -*- coding: utf-8 -*-
import random


IMAGES = ['''

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
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

tries = 0
WORD_LIST = ['CASA', 
             'PERRO',
             'COMPUTADORA',
             'EMPRESA',
             'SOFA',
             'BICICLETA',
             'LIBERTAD']

def random_word(WORD_LIST):
    random_index = random.randint(0,len(WORD_LIST) - 1)
    return WORD_LIST[random_index]



def show_dashboar(hiden_word, tries):
    print(IMAGES[tries])
    print(hiden_word)
        



def run():
    word = random_word(WORD_LIST)
    hiden_word = ('*-*') * len(word)
    
    while True:
        
        show_dashboar(hiden_word, tries)
        current_letter = (str(input('Dime una letra: '))).upper()
        print(word)


        if current_letter in word :
            print('la letra {} esta en la parabra'.format(current_letter))
            
            idx_to_change = []
            idx_in_word = 0
            
            for letter in word:
                if letter == current_letter:
                    
                    idx_to_change.append(idx_in_word)
                    print(idx_to_change)
                idx_in_word += 1 


if __name__ == '__main__':

    print('B I E N V E N I D O S   A   A H O R C A D O S')
    run()