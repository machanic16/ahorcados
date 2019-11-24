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

WORD_LIST = ['CASA', 
             'PERRO',
             'COMPUTADORA',
             'EMPRESA',
             'SOFA',
             'BICICLETA',
             'LIBERTAD']

def random_word(WORD_LIST):
    ''' This function return a random word from word list'''
    random_index = random.randint(0,len(WORD_LIST) - 1)
    return WORD_LIST[random_index]



def show_dashboar(hiden_word, tries):
    ''' Show the dashboard'''
    print(IMAGES[tries])
    print(hiden_word)
        



def run():
    ''' Starts the game'''
    tries = 0
    word = random_word(WORD_LIST)
    hiden_word = ['*-*'] * len(word)
    non_alpha_type = 0
    
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
            
            for idx in idx_to_change:
                hiden_word[idx] = current_letter
            
            try:
                hiden_word.index('*-*')
            except ValueError:
                print('')
                print(' Fleicidades ganaste, la palabra es {}'.format(word))
                break
        
        elif current_letter.isalpha() :
            if non_alpha_type == 0:
                print('Solo puedes usar letras, de ahora en adelante estos tambien contaran como errores')
                non_alpha_type += 1
            else:
                tries += 1

        else:
            print('La letra {} NO esta en la palabra')
            if tries < len(IMAGES) - 1:
                tries += 1
            else:
                print('Perdiste .-.')
                break            

    #show_dashboar('hola', tries)

if __name__ == '__main__':

    print('B I E N V E N I D O S   A   A H O R C A D O S')
    run()
