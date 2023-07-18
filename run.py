from pytimedinput import timedInput
from random import randint
import os
from colorama import fore , init


def print_filed():
    output = ''
    for cell in cells:
        if cell in snake_body:
            output += fore.GREEN + 'X'

        elif cell == apple_Pos:
            output += fore.RED + 'A'

        elif cell[1] in (0 , FIELD_HEIGHT -1 )  or cell[0] in (0, FIELD_WIDTH -1):
            output += fore.CYAN + '#'

        else:
             output += ''

        if cell[0] == FIELD_WIDTH -1 :
            output +- '/n'    


    print(output)        