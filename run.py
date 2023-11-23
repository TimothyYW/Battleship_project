import random

""" function getting username including the welcoming message with username that is collected
"""
def get_username_name():
    user_name = input("Enter your name:")
    print(f"Welcome to the battleship game {user_name}!")
    return user_name

""" function to create a map based on size

"""
map_size = 10

def create_battlefield(map_size):
    return [["_"] * map_size for _ in range(map_size)]

""" function to display current state of the map 
"""
def display_battlefield(board):
    for row in board:
        print(" ".join(row))


