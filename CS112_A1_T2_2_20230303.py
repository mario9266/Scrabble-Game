# File: CS112_A1_T2_2_20230303.py
# Purpose: Two players pick numbers from 1 to 9 to reach a sum of 15 if no ones sum is 15 they draw
# Author: Mario George Halim Ibrahim
# ID: 20230303

# Function to print the available numbers
def print_board(available_numbers):
    print("Available numbers:", available_numbers)


# Function to check if a player has won
def is_winner(numbers):
    return sum(numbers) == 15


def number_scrabble():
    # Create variables for available numbers and create a list of numbers from 1 to 9
    available_numbers = list(range(1, 10))
    player1_numbers = []
    player2_numbers = []

    # Main game loop continues until there are no available numbers
    while available_numbers:
        print_board(available_numbers)

        while True:
            selected_number = input("Player 1, choose a number: ")

            # Checks input availability
            if not selected_number.isdigit():
                print("Invalid input! Please enter a number.")
                continue

            selected_number = int(selected_number)
            if selected_number not in available_numbers:
                print("Invalid number! Try again.")
            else:
                break

        # Update game state
        available_numbers.remove(selected_number)
        player1_numbers.append(selected_number)

        # Check if player 1 wins or a draw
        if is_winner(player1_numbers):
            print("Player 1 wins!")
            return

        if not available_numbers:
            print("It's a draw!")
            return

        # Print the updated available numbers
        print_board(available_numbers)

        while True:
            selected_number = input("Player 2, choose a number: ")

            # Checks input availability
            if not selected_number.isdigit():
                print("Invalid input! Please enter a number.")
                continue
            selected_number = int(selected_number)
            if selected_number not in available_numbers:
                print("Invalid number! Try again.")
            else:
                break

        # Update game state
        available_numbers.remove(selected_number)
        player2_numbers.append(selected_number)

        # Check if player 2 wins or a draw
        if is_winner(player2_numbers):
            print("Player 2 wins!")
            return

        if not available_numbers:
            print("It's a draw!")
            return


number_scrabble()
