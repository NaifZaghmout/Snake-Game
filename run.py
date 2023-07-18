from pytimedinput import timedInput
from random import randint
import os
from colorama import Fore, init


def print_filed():
    output = ''
    for cell in cells:
        if cell in snake_body:
            output += fore.GREEN + 'X'

        elif cell == apple_Pos:
            output += fore.RED + 'A'

        elif cell[1] in (0, FIELD_HEIGHT - 1) or cell[0] in (0, FIELD_WIDTH - 1):
            output += fore.CYAN + '#'

        else:
            output += ''

        if cell[0] == FIELD_WIDTH - 1:
            output + - '/n'



    print(output)




def update_snake():
    global has_eaten
    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
    snake_body.insert(0, new_head)
    if not has_eaten:
        snake_body.pop[-1]
    has_eaten = False



