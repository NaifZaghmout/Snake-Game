from pytimedinput import timedInput
from random import randint
import os
from colorama import Fore, init


def print_filed():
    '''
    Prints a play field
    '''
    output = ''
    for cell in cells:
        if cell in snake_body:  # Checking if the snake is in the cell
            output += Fore.GREEN + 'x'

        elif cell == apple_Pos:
            output += Fore.RED + '*'

        elif cell[1] in (0, FIELD_HEIGHT - 1) or cell[0] in (0, FIELD_WIDTH - 1):
            output += Fore.CYAN + '-'

        else:
            output += ' '

        if cell[0] == FIELD_WIDTH - 1:
            output += '\n'

    os.system('clear')
    print(output)


def update_snake():
    global has_eaten, direction
    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
    snake_body.insert(0, new_head)
    if not has_eaten:
        snake_body.pop(-1)
    has_eaten = False

    if snake_body[0][1] in (0, FIELD_HEIGHT - 1) or snake_body[0][0] in (0, FIELD_WIDTH - 1):

        direction = (-direction[0], -direction[1])

    if snake_body[0] in snake_body[1:]:
        os.system('clear')
        print('Game Over!')
        global play_again
        play_again = False


def apple_cllision():
    global apple_Pos, has_eaten

    if snake_body[0] == apple_Pos:
        apple_Pos = place_apple()
        has_eaten = True


def place_apple():
    col = randint(1, FIELD_WIDTH - 2)
    row = randint(1, FIELD_HEIGHT - 2)
    while (col, row) in snake_body:
        col = randint(1, FIELD_WIDTH - 2)
        row = randint(1, FIELD_HEIGHT - 2)
    return (col, row)


init(autoreset=True)


FIELD_WIDTH = 25
FIELD_HEIGHT = 15
cells = [(col, row) for row in range(FIELD_HEIGHT)
         for col in range(FIELD_WIDTH)]


snake_body = [
    (7, FIELD_HEIGHT // 2),
    (6, FIELD_HEIGHT // 2),
    (5, FIELD_HEIGHT // 2)
]


directions = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
direction = directions['right']
has_eaten = False
apple_Pos = place_apple()


play_again = True


# ... (previous code remains the same)

while play_again:
    snake_body = [
        (7, FIELD_HEIGHT // 2),
        (6, FIELD_HEIGHT // 2),
        (5, FIELD_HEIGHT // 2)
    ]

    direction = directions['right']
    has_eaten = False
    apple_Pos = place_apple()

    while play_again:
        if has_eaten:
            apple_Pos = place_apple()
            has_eaten = False

        print_filed()

        text, _ = timedInput('', timeout=0.3)
        match text:
            case 'w':
                direction = directions['up']
            case 'a':
                direction = directions['left']
            case 's':
                direction = directions['down']
            case 'd':
                direction = directions['right']
            case 'q':
                os.system('clear')
                play_again = False
                break

        update_snake()
        apple_cllision()

        if snake_body[0][1] in (0, FIELD_HEIGHT - 1) or \
                snake_body[0][0] in (0, FIELD_WIDTH - 1) or \
                snake_body[0] in snake_body[1:]:
            os.system('clear')
            print('Game Over!')
            break

    print("Play again? (y/n)")
    while True:
        choice = input().lower()
        if choice in ('y', 'n'):
            break
        print("Invalid choice. Please enter 'y' or 'n'.")

    if choice != 'y':
        play_again = False
    else:
        play_again = True
