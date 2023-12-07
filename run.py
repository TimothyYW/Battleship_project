from random import randrange


ship_initial = ["B", "C", "F", "A", "S"]
ship_names = ["Battleship", "Cruiser", "Frigate", "Aircraft Carrier", "Sub"]
map_size = 10

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


def guide_rule():
    """
    function to display rule for the game
    """
    print("rule of game: ")
    print("there are 5 ships for player and computer")
    print("give them coordinate for row and column from 0 to 10")
    print("once 5 ships from enemy or the player has been sunk, the game will be over")


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


def check_player_hit(comp_board, fake_board, user):
    """
    function for player hit or missed on enemy ship
    """
    user_name = user
    while True:
        try:
            print(f"{user} coordinates")
            row = int(input("Enter your target row: "))
            col = int(input("Enter your target col: "))
            hit = 1

            if comp_board[row][col] == "B":
                fake_board[row][col] = "B" 
                print("Computer: Battleship been hit!")
            elif comp_board[row][col] == "C":
                fake_board[row][col] = "C"
                print("Computer: Cruiser been hit!")
            elif comp_board[row][col] == "F":
                fake_board[row][col] = "F"
                print("Computer: Frigate been hit!")
            elif comp_board[row][col] == "A":
                fake_board[row][col] = "X"
                print("Computer: Aircraft Carrier been hit")
            elif comp_board[row][col] == "S":
                fake_board[row][col] = "S"
                print("Computer: Sub been hit")
            else:
                fake_board[row][col] = "*"
                hit = 0  
                print("Missed me!")

            break

        except ValueError:
            print("Invalid number. Please enter valid number")
        except IndexError:
            print("Please select between 0 to 9")

    return hit

def check_comp_hit(player_board):
    """
    function for comp hit or missed on the player ship
    """

    hit = 1
    
    while True:
        row = randrange(0, 10)
        col = randrange(0, 10)
        if (player_board[row][col] != "*",
            player_board[row][col] != "A",
            player_board[row][col] != "B",
            player_board[row][col] != "C",
            player_board[row][col] != "F",
            player_board[row][col] != "S"):
            break

    print("Computer has selected coordinates", row, col)

    if player_board[row][col] == "B":
        player_board[row][col] = "B"
        print("Player: Battleship been hit!")
    elif player_board[row][col] == "C":
        player_board[row][col] = "C"
        print("Player: Cruiser been hit!")
    elif player_board[row][col] == "F":
        player_board[row][col] = "F"
        print("Player: Frigate been hit!")
    elif player_board[row][col] == "A":
        player_board[row][col] = "A"
        print("Player: Aircraft carrier been hit!")
    elif player_board[row][col] == "S":
        player_board[row][col] = "S"
        print("Player: Sub been hit!")
    else:
        hit = 0
        print("Missed me!")
        player_board[row][col] = "*"

    return hit


if __name__ == "__main__":

        user = get_username()

        guide_rule()

        player_board = create_battlefield(map_size)
        comp_board = create_battlefield(map_size)
        fake_board = create_battlefield(map_size)

        occupied = set()

        print("Player's turn:")
        player_ship_coordinate(player_board, occupied)
        display_battlefield(player_board)

        print("\nComputer opponent's turn:")
        comp_ship_coordinate(comp_board)
        display_battlefield(comp_board)
        # display_battlefield(fake_board)

        player_hits = 0
        comp_hits = 0

        while True:
            player_hits += check_player_hit(comp_board, fake_board, user)
            if player_hits == 5:
                print("Player has won - game over")
                break

            comp_hits += check_comp_hit(player_board)
            if comp_hits == 5:
                print("Computer has won - game over")
                break

            print(f"Player {user} board")
            display_battlefield(player_board)
                    
            print(" ")

            print("Computer board")
            display_battlefield(fake_board)