from random import randrange


shipIntial = ["B", "C", "F", "A", "S"]
shipNames = ["Battleship", "Cruiser", "Frigate", "Aircraft Carrier", "Sub"]


def get_username_name():
    """
    function getting username for welcome message
    """
    user_name = input("Enter your name:")
    print(f"Welcome to the battleship game {user_name}!")
    return user_name


map_size = 10


def create_battlefield(map_size):
    """
    function to create a map based on size
    """
    return [["_"] * map_size for _ in range(map_size)]


def display_battlefield(board):
    """
    function to display current state of the map 
    """
    for row in board:
        print(" ".join(row))


def player_ship_coordinate(player_board):
    """
    function for player placement ship
    """
    while True:
        try:
            row = int(input("Enter the row for Battleship: "))
            col = int(input("Enter the column for Battleship: "))         
            if 0 <= row < 10 and 0 <= col < 10:
                player_board[row][col] = "B"
                break
            else:
                print("Invalid coordinates. Please enter correct value.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Cruiser: "))
            col = int(input("Enter the column for Cruiser: "))
            
            if 0 <= row < 10 and 0 <= col < 10:
                player_board[row][col] = "C"
                break
            else:
                print("Invalid coordinates. Please enter correct values.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    while True:
        try:
            row = int(input("Enter the row for Frigate: "))
            col = int(input("Enter the column for Frigate: "))
            if 0 <= row < 10 and 0 <= col < 10:
                player_board[row][col] = "F"
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Aircraft Carrier: "))
            col = int(input("Enter the column for Aircraft Carrier: "))
            
            if 0 <= row < 10 and 0 <= col < 10:
                player_board[row][col] = "A"
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Submarine: "))
            col = int(input("Enter the column for Submarine: "))
            
            if 0 <= row < 10 and 0 <= col < 10:
                player_board[row][col] = "S"
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return playerBoard


def comp_ship_coordinate(compBoard):
    """
    function for computer opponent
    """
    for _ in range(5):
        row = randrange(0, 10)
        col = randrange(0, 10)
        compBoard[row][col] = "B"
    
    for _ in range(3):
        row = randrange(0, 10)
        col = randrange(0, 10)
        compBoard[row][col] = "C"

    for _ in range(4):
        row = randrange(0, 10)
        col = randrange(0, 10)
        compBoard[row][col] = "F"

    for _ in range(6):
        row = randrange(0, 10)
        col = randrange(0, 10)
        compBoard[row][col] = "A"

    for _ in range(2):
        row = randrange(0, 10)
        col = randrange(0, 10)
        compBoard[row][col] = "S"

    return compBoard


def check_player_hit(compBoard, playerHit):
    """
    function for player hit or missed on enemy ship
    """
    row = int(input("Enter your row: "))
    col = int(input("Enter your col:"))

    if compBoard[row][col] == "B"
        playerHit[row][col] == "B"
        print("Computer: Battleship been hit!")
    elif: 
        compBoard[row][col] == "C"
        playerHit[row][col] == "C"
        print("Computer: Cruiser been hit!")
    elif:
        compBoard[row][col] == "F"
        playerHit[row][col] == "F"
        print("Computer: Frigate been hit!")
    elif:
        compBoard[row][col] == "A"
        playerHit[row][col] == "A"
        print("Computer: Aircraft Carrier been hit")
    elif:
        compBoard[row][col] == "S"
        playerHit[row][col] == "S"
        print("Computer: Sub been hit")
    else:
        playerHit[row][col] == "M"
        print("Missed me!")

    return playerHit
    
if __name__ == "__main__":
    playerboard = create_battlefield(map_size)
    compboard = create_battlefield(map_size)

    print("Player's turn:")
    player_ship_coordinate(playerboard)
    display_battlefield(playerboard)

    print("\nComputer opponent's turn:")
    comp_ship_coordinate(compboard)
    display_battlefield(compboard)
