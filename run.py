import random
"""
function getting username including the welcoming message with username that is collected
"""
def get_username_name():
    user_name = input("Enter your name:")
    print(f"Welcome to the battleship game {user_name}!")
    return user_name

get_username_name()