from random import randrange


shipIntial = ["B", "C", "F", "A", "S"]
shipNames = ["Battleship", "Cruiser", "Frigate", "Aircraft Carrier", "Submarine"]



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



def player_ship_coordinate(playerBoard):
    """
    function for player placement ship
    """
    for B in range(5):
        try:
            row = int(input("Enter the row for Battleship (0-9): "))
            col = int(input("Enter the column for Battleship (0-9): "))
            
            if 0 <= row < 10 and 0 <= column < 10:
                playerBoard[row][col] = "B"
            else:
                print("Invalid coordinates. Please enter values between 0 and 9.")
                B -= 1  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for C in range(3):
        try:
            row = int(input("Enter the row for Cruiser (0-9): "))
            col = int(input("Enter the column for Cruiser (0-9): "))
            
            if 0 <= row < 10 and 0 <= column < 10:
                playerBoard[row][col] = "C"
            else:
                print("Invalid coordinates. Please enter values between 0 and 9.")
                C -= 1  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    for F in range(4):
        try:
            row = int(input("Enter the row for Frigate (0-9): "))
            column = int(input("Enter the column for Frigate (0-9): "))
            
            if 0 <= row < 10 and 0 <= column < 10 and playerBoard[row][column] == "_":
                playerBoard[row][column] = "F"
            else:
                print("Invalid coordinates. Please enter values between 0 and 9 or choose an unoccupied position.")
                F -= 1  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for A in range(6):
        try:
            row = int(input("Enter the row for Aircraft Carrier (0-9): "))
            column = int(input("Enter the column for Aircraft Carrier (0-9): "))
            
            if 0 <= row < 10 and 0 <= column < 10 and playerBoard[row][column] == "_":
                playerBoard[row][column] = "A"
            else:
                print("Invalid coordinates. Please enter values between 0 and 9 or choose an unoccupied position.")
                A -= 1  # Decrement A to re-enter the coordinates
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for S in range(2):
        try:
            row = int(input("Enter the row for Submarine (0-9): "))
            column = int(input("Enter the column for Submarine (0-9): "))
            
            if 0 <= row < 10 and 0 <= column < 10 and playerBoard[row][column] == "_":
                playerBoard[row][column] = "S"
            else:
                print("Invalid coordinates. Please enter values between 0 and 9 or choose an unoccupied position.")
                S -= 1  # Decrement S to re-enter the coordinates
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    return playerBoard


def comp_ship_coordinate(compBoard):
    """
    function for computer opponent
    """

    for B in range(5):
        x = randrange(0, 10)
        y = randrange(0, 10)
        compBoard[x][y] = "A"
    
    for C in range(3):
        x1 = randrange(0, 10)
        y1 = randrange(0, 10)
        compBoard[x1][y1] = "C"

    for F in range(4):
        x2 = randrange(0, 10)
        y2 = randrange(0, 10)
        compBoard[x2][y2] = "F"

    for A in range(6):
        x3 = randrange(0, 10)
        y3 = randrange(0, 10)
        compBoard[x3][y3] = "A"

    for S in range(2):
        x4 = randrange(0, 10)
        y4 = randrange(0, 10)
        compBoard[x4][y4] = "S"

    return compBoard
    
if __name__ == "__main__":
    playerboard = create_battlefield(map_size)
    compboard = create_battlefield(map_size)

    print("Player's turn:")
    player_ship_coordinate(playerboard)
    display_battlefield(playerboard)

    print("\nComputer opponent's turn:")
    comp_ship_coordinate(compboard)
    display_battlefield(compboard)
