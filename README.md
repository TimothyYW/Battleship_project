# Battleship game

Welcome to the battleship game, a game runs on the Python terminal.

user will be up against enemy AI, both player and computer will have 5 ships with their own initial and user must destroy all of opponent ships before all of their own ships sunk.

Here is my active project

![Battleship game]

## How to play

Battleship game based on the project suggestion by code institute.

In this version, user need to input their username first.

Afterward, player should input their ships coordinate, those are:

Battleship, Frigate, Cruiser, Aircraft carrier, and (Sub)marine.

The player will be able to see their ships placement after input valid coodinates.

They will be market with their initial:

- Battleship = B

- Frigate = F

- Cruiser = C

- Aircraft carrier = A

- Submarine = S

After input the coordinate for each ships, player will be able to input coordinate to where they would like to fire a shot.

If player missed it will display " * ", while if it was a hit it will be shown by X.

While the computer coordinates will be randomize and the player must guess where the ships are.

Player and computer will be take turn to discover the ship location.

In order to win the game either player or computer must sunk all 5 ships.

## Features

# Existing feature

- Customize board

    - Player allowed to choose where do they want to put their board.

    - Different initial for different ships.

![Player board]

- Computer board

    - Computer board will generate random.

    - Computer board will only shows the ship that been hit.

![Computer board]

- Error
## Future feature

- Adding different sizes for the ship.

- Allowing player choose to put ships horizontal or vertical.

## Data Model


## Testing

I have used couple of methods to check the game function:

    - passed the code PEP8, no error occur.
    - Invalid input will be respond with asking for valid numbers or that has not been picked.
    - 

## Bugs

# Solved bug

- When I input an alphabet instead of number, it will crash the game. I resolve this by creating message for ValueError and IndexError.

- Map refuse to print out after every turn, just add break command to break the loop.

# Remaining bug

- No bugs remaining.

# Validator test

- PEP 8

    - No error result

## Credit

Code institute suggestion for Project.

Colorama 

https://pypi.org/project/colorama/

Installation

https://medium.com/@sim30217/pip-freeze-requirements-txt-993eb433ab0b#:~:text=Apr%207-,pip%20freeze%20%3E%20requirements.,along%20with%20their%20corresponding%20versions

Embedded diffrent colors

https://www.youtube.com/shorts/GtGPq2eXBz0

Battleship design suggestion

https://stackoverflow.com/questions/28866424/making-simple-game-of-battleship

https://stackoverflow.com/questions/14181146/codeacademy-battleship-project-syntax-error

https://www.youtube.com/watch?v=MgJBgnsDcF0

https://copyassignment.com/battleship-game-code-in-python/#google_vignette

https://stackoverflow.com/questions/55759918/battleship-game-in-python-for-a-project-in-school

