# -*- coding: utf-8 -*-
import random

''' ASCII art para el avance del juego'''
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
    print(IMAGES[tries])
    print(hiden_word)
        
def end_game(word):
    print('Perdiste el juego la palabra era {}'.format(word))
    
      


def run():
    ''' Starts the game'''
    tries = 0
    last_trie = len(IMAGES) 
    word = random_word(WORD_LIST)
    hiden_word = ['*-*'] * len(word)
    first_time_non_alpha_type = True
    first_time_retype_letter = True
    
    while True:
        
        show_dashboar(hiden_word, tries)
        current_letter = (str(input('Dime una letra: '))).upper()

        if current_letter in hiden_word :
            if first_time_retype_letter :
                print('La letra {} ya la escribiste. de ahora en adelante contara como un error'.format(current_letter))
                first_time_retype_letter = False
            else:
                tries += 1
            
            if tries == last_trie:
                end_game(word)
                break


        elif current_letter in word :
            print('la letra {} esta en la parabra'.format(current_letter))
            
            idx_to_change_in_hiden_word = []
            idx_in_word = 0
            
            for letter in word:
                if letter == current_letter:
                    
                    idx_to_change_in_hiden_word.append(idx_in_word)
                    print(idx_to_change_in_hiden_word)
                idx_in_word += 1 
            
            for idx in idx_to_change_in_hiden_word:
                hiden_word[idx] = current_letter
            
            try:
                hiden_word.index('*-*')
            except ValueError:
                print('')
                print(' Fleicidades ganaste, la palabra es {}'.format(word))
                break
        
        elif not current_letter.isalpha() :
            if first_time_non_alpha_type :
                print('Solo puedes usar letras, de ahora en adelante estos tambien contaran como errores')
                first_time_non_alpha_type = False
            else:
                tries += 1
            
            if tries == last_trie  :
                end_game(word)
                break   
            
        

        else:
            print('La letra {} NO esta en la palabra'.format(current_letter))
            
            tries += 1

            if tries == last_trie :
                end_game(word)
                break            


if __name__ == '__main__':

    print('B I E N V E N I D O S   A   A H O R C A D O S')
    run()
