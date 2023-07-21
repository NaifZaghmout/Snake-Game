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
        if cell in snake_body:          # Checking if the snake is in the cell
            output += Fore.GREEN + 'X'  # print the snake body in green

        elif cell == apple_Pos:
            output += Fore.RED + 'o'    # print the apple in red

        elif cell[1] in (0, FIELD_HEIGHT - 1) or cell[0] in (0, FIELD_WIDTH - 1):
            output += Fore.CYAN + '*'    # # Print the boundaries in cyan

        else:
            output += ' '                # print the empty space

        if cell[0] == FIELD_WIDTH - 1:
            output += '\n'               # move to the next line after printing each row

    os.system('clear')
    # clear the console and print the play field
    print(output)


def update_snake():
    '''
    function to update the snake position 
    '''

    global has_eaten, direction
    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
    # move the snake head to the new position
    snake_body.insert(0, new_head)
    if not has_eaten:
        # remove the tail if the snake hasn't eaten an apple
        snake_body.pop(-1)
    has_eaten = False

    if snake_body[0][1] in (0, FIELD_HEIGHT - 1) or snake_body[0][0] in (0, FIELD_WIDTH - 1):

        # Reverse the direction when hitting a boundary
        direction = (-direction[0], -direction[1])

    if snake_body[0] in snake_body[1:]:
        os.system('clear')
        # Print "Game Over!" when the snake collides with itself
        print('Game Over!')
        global play_again
        play_again = False                 # End the game


def apple_cllision():
    '''
    Function to handle apple collision
    '''

    global apple_Pos, has_eaten

    if snake_body[0] == apple_Pos:
        apple_Pos = place_apple()          # Generate a new apple position
        has_eaten = True                   # Indicate that the snake has eaten the apple


def place_apple():
    '''
     Function to generate a new random position for the apple
    '''
    col = randint(1, FIELD_WIDTH - 2)
    row = randint(1, FIELD_HEIGHT - 2)
    while (col, row) in snake_body:
        col = randint(1, FIELD_WIDTH - 2)
        row = randint(1, FIELD_HEIGHT - 2)
    return (col, row)


init(autoreset=True)


# Set the size of the play field
FIELD_WIDTH = 25
FIELD_HEIGHT = 15
cells = [(col, row) for row in range(FIELD_HEIGHT)    # Generate all cells in the play field
         for col in range(FIELD_WIDTH)]


# Initialize the snake's starting position and direction
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

# Game loop starts here
while play_again:
     # Reinitialize the snake's position and direction
    snake_body = [
        (7, FIELD_HEIGHT // 2),
        (6, FIELD_HEIGHT // 2),
        (5, FIELD_HEIGHT // 2)
    ]

    direction = directions['right']
    has_eaten = False
    apple_Pos = place_apple()

    # Inner game loop for handling input and updating the game state
    while play_again:
        if has_eaten:
            apple_Pos = place_apple()
            has_eaten = False

        print_filed()                # Print the current play field

        # Read user input with a timeout
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

        
        update_snake()                      # Update the snake's position and check for collisions
        apple_cllision()                    # Check if the snake has eaten the apple

        if snake_body[0][1] in (0, FIELD_HEIGHT - 1) or \
                snake_body[0][0] in (0, FIELD_WIDTH - 1) or \
                snake_body[0] in snake_body[1:]:
            os.system('clear')
            print('Game Over!')             # Print "Game Over!" when the snake coll
            break

    print("Play again? (y/n)")
    '''
    ask the user to play again or not
    '''
    while True:
        choice = input().lower()
        if choice in ('y', 'n'):              # Check if the user's choice is y or n
            break
        # Print an error message if the user enters an invalid choice
        print("Invalid choice. Please enter 'y' or 'n'.")

    if choice != 'y':
        # Set play_again to False if the user chose not to play again
        play_again = False
    else:
        # Set 'play_again' to True if the user chose to play again
        play_again = True

