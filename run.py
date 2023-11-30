from random import randrange


ship_initial = ["B", "C", "F", "A", "S"]
ship_names = ["Battleship", "Cruiser", "Frigate", "Aircraft Carrier", "Sub"]


def get_username():
    """
    function getting username for welcome message
    """
    while True:
        user_name = input("Enter your name:")
        if user_name:
            print(f"Welcome to the battleship game {user_name}!")
            return user_name
        else:
            print("Please enter your name.")


map_size = 10


def create_battlefield(map_size):
    """
    function to create a map based on size
    """
    return [["_"] * map_size for _ in range(map_size)]


def display_battlefield(board):
    """
    function to display current state of the map.
    """
    for row in board:
        print(" ".join(row))


def player_ship_coordinate(player_board, occupied):
    """
    function for player placement ship
    """
    while True:
        try:
            row = int(input("Enter the row for Battleship: "))
            col = int(input("Enter the column for Battleship: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "B"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct value.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Cruiser: "))
            col = int(input("Enter the column for Cruiser: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "C"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct values.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Frigate: "))
            col = int(input("Enter the column for Frigate: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "F"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Aircraft Carrier: "))
            col = int(input("Enter the column for Aircraft Carrier: "))

            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "A"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Submarine: "))
            col = int(input("Enter the column for Submarine: "))

            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "S"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return player_board, occupied


def comp_ship_coordinate(comp_board):
    """
    function for computer opponent.
    """
    for ship in ship_initial:
        while True:
            row = randrange(0, 10)
            col = randrange(0, 10)
            if comp_board[row][col] == "_":
                comp_board[row][col] = ship
                break

    return comp_board


def check_player_hit(comp_board, player_hit):
    """
    function for player hit or missed on enemy ship
    """
    row = int(input("Enter your row: "))
    col = int(input("Enter your col:"))

    if comp_board[row][col] == "B":
        player_hit[row][col] = "B"
        print("Computer: Battleship been hit!")
    elif comp_board[row][col] == "C":
        player_hit[row][col] = "C"
        print("Computer: Cruiser been hit!")
    elif comp_board[row][col] == "F":
        player_hit[row][col] = "F"
        print("Computer: Frigate been hit!")
    elif comp_board[row][col] == "A":
        player_hit[row][col] = "A"
        print("Computer: Aircraft Carrier been hit")
    elif comp_board[row][col] == "S":
        player_hit[row][col] = "S"
        print("Computer: Sub been hit")
    else:
        player_hit[row][col] = "M"
        print("Missed me!")

    return player_hit


def check_comp_hit(player_board, comp_hit):
    """
    function for comp hit or missed on the player ship
    """
    row = (int(input("Enter your coordinate: ")))
    col = (int(input("Enter your coordinate: ")))

    if player_board[row][col] == "B":
        comp_hit[row][col] = "B"
        print("Player: Battleship been hit!")
    elif player_board[row][col] == "C":
        comp_hit[row][col] = "C"
        print("Player: Cruiser been hit!")
    elif player_board[row][col] == "F":
        comp_hit[row][col] = "F"
        print("Player: Frigate been hit!")
    elif player_board[row][col] == "A":
        comp_hit[row][col] = "A"
        print("Player: Aircraft carrier been hit!")
    elif player_board[row][col] == "S":
        comp_hit[row][col] = "S"
        print("Player: Sub been hit!")
    else:
        comp_hit[row][col] = "M"
        print("Missed me!")

    return comp_hit


if __name__ == "__main__":

        get_username()

        player_board = create_battlefield(map_size)
        comp_board = create_battlefield(map_size)

        occupied = set()

        print("Player's turn:")
        player_ship_coordinate(player_board, occupied)
        display_battlefield(player_board)

        print("\nComputer opponent's turn:")
        comp_ship_coordinate(comp_board)
        display_battlefield(comp_board)
