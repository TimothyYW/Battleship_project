import random from random

shipIntial = ["B", "C", "F", "A", "S"]
shipNames = ["Battleship", "Cruiser", "Frigate", "Aircraft Carrier", "Submarine"]


"""
function getting username for welcome message
"""
def get_username_name():
    user_name = input("Enter your name:")
    print(f"Welcome to the battleship game {user_name}!")
    return user_name

""" 
function to create a map based on size
"""

map_size = 10

def create_battlefield(map_size):
    return [["_"] * map_size for _ in range(map_size)]

""" 
function to display current state of the map 
"""

def display_battlefield(board):
    for row in board:
        print(" ".join(row))

"""
function for player placement ship
"""

def player_ship_coordinate(playerBoard):

    for B in range(5):
        x, y = (int(input("Enter your coordinate for Battleship:")))
        playerBoard [x][y] = "B"

    for C in range(3):
        x1, y1 = (int(input("Enter your coordinate for Cruiser: ")))
        playerBoard [x1][y1] = "C"

    for F in range(4):
        x2, y2 = (int(input("Enter your coordinate for Frigate: ")))
        playerBoard [x2][y2] = "F"

    for A in range(6):
        x3, y3 = (int(input("Enter your coordinate for Aircraft carrier: ")))
        playerBoard [x3][y3] = "A"

    for S in range(2):
        x4, y4 = (int(input("Enter your coordinate for Submarine: ")))
        playerBoard [x4][y4] = "S"
    

