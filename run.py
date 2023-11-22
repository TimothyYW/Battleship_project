import random

"""
function getting username including the welcoming message with username that is collected
"""
def get_username_name():
    user_name = input("Enter your name:")
    print(f"Welcome to the battleship game {user_name}!")
    return user_name

"""
function to print the board for the game
"""
map_size = 10

def create_battlefield(map_size):
    
    return [["_"] * map_size for _ in range(map_size)]


print(create_battlefield(map_size))