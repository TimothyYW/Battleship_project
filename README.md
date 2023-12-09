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



## Future feature

- Adding different sizes for the ship.

- Allowing player choose to put ships horizontal or vertical.

## Data Model

## Testing

## Bugs

# Solved bug

- When I input an alphabet instead of number, it will crash the game. I resolve this by creating message for ValueError and IndexError

# Remaining bug

- When input coordinate to attack, it will just only said player missed or hit without update the map display.

- Enemy opponent did not choose coordinate nor try to attack player.

# Validator test

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

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
