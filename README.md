# Battleship game

Welcome to the battleship game, a game runs on the Python terminal.

user will be up against enemy AI, both player and computer will have 5 ships with their own initial and user must destroy all of opponent ships before all of their own ships sunk.

Here is my project mock up test result.

![Battleship game](assets/images/Mock-up-result.png)

[Link to deployed site](https://battleship-games-b1b85efb0396.herokuapp.com/)

## How to play

Battleship game based on the project suggestion by code institute.

In this version, user need to input their username first.

Afterward, player should input their ships coordinate, those are:

Battleship, Frigate, Cruiser, Aircraft carrier, and (Sub)marine.

The player will be able to see their ships placement after input valid coodinates.

They will be market with their initial and color:

- Battleship = B Red

- Frigate = F Cyan

- Cruiser = C Green

- Aircraft carrier = A Blue

- Submarine = S Yellow

After input the coordinate for each ships, player will be able to input coordinate to where they would like to fire a shot.

If player missed it will display " * ", while if it was a hit it will be shown by X.

While the computer coordinates will be randomize and the player must guess where the ships are.

Player and computer will be take turn to discover the ship location.

In order to win the game either player or computer must sunk all 5 ships.

# Features

## Existing feature

- Customize board

    - Player allowed to choose where do they want to put their board.

    - Different initial for different ships.

![Ship Placement example](assets/images/Ship-placement.png)

![Player board](assets/images/Player-board.png)

- Computer board

    - Computer board will generate random.

    - Computer board will only shows the ship that been hit.

![Computer board](assets/images/Player-and-computer-board%20-%20Copy.png)

- Input valdation error:

    - User need to enter the row and col from 0 to 9

![If coordinate above 9 or below 0](assets/images/bigger-number%20-%20Copy.png)

    - User need to pick a valid coordinate

![Invalid message](assets/images/invalid-coordinate.png)

- User of colorama:

    - If player and computer missed the message will be highlighted by color

![Missed message](assets/images/Missed-message.png)

    - If ship been hit the message will be highlighted also.

![Example of ship been hit](assets/images/Example-ship.png)

# Future feature

- Adding different sizes for the ship.

- Allowing player choose to put ships horizontal or vertical.

# Data Model

The based model is from the battleship game with bigger map. Similar system which shows the player board while the empty board belong to the computer.

The create_battlefield will be creating boards for both side, display_battlefield will be displaying player board and computer board, above the board will be written player turn and computer turn.

The board model also make it easier to keep track of the situation combining with create_battlefield and display_battlefield function. 

# Testing

I have used couple of methods to check the game function:

    - passed the code PEP8, no error occur.
    - Invalid input will be respond with asking for valid numbers or that has not been picked.
    - Testing through heroku result is no error occur.

# Bugs

## Solved bug

- When I input an alphabet instead of number, it will crash the game. I resolve this by creating message for ValueError and IndexError.

- Map refuse to print out after every turn, just add break command to break the loop.

## Remaining bug

- No bugs remaining.

# Validator test

- PEP 8

    - No error result

# Deployment

This project was deployed through heroku:

Follow the step below:

- Create heroku app

- Add name for the app

- Choose either Europe or United State

- Set the buildbacks first to Python and afterward NodeJS

- Add The key is PORT and the value is 8000 to the Config Vars

- Connect to GitHub and then search for the project by the name

- Click Deploy

# Credit

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

