import random
import sys


# Class for formatting the terminal.
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def make_decision(user_choice):
    """
    Function that checks, if the user won, lost or has a draw against the pc
    :param user_choice:
    :return: user_won, user_lost or user_draw
    """

    # Make users choice lowercase
    user_choice = user_choice.lower()
    # Let the computer choose a number between 1 and 3 and convert it to the corresponding choice
    pc_choice = random.randint(1, 3)
    if pc_choice == 1:
        pc_choice = 'rock'
    elif pc_choice == 2:
        pc_choice = 'paper'
    else:
        pc_choice = 'scissors'

    # Print the users and computers choice
    print("Your choice: " + user_choice)
    print("My choice: " + pc_choice)

    # Return if the user won, lost or if it's a draw
    if (user_choice == 'rock' and pc_choice == 'scissors') or (user_choice == 'paper' and pc_choice == 'rock') or \
            (user_choice == 'scissors' and pc_choice == 'paper'):
        return 'user_won'
    elif (user_choice == 'rock' and pc_choice == 'paper') or (user_choice == 'paper' and pc_choice == 'scissors') or \
            (user_choice == 'scissors' and pc_choice == 'rock'):
        return 'user_lost'
    else:
        return 'user_draw'


def main():
    print('***************************************')
    print('*                                     *')
    print('* The Lux\' Rock, Paper, Scissors Game *')
    print('*                                     *')
    print('***************************************')
    print()
    print('Welcome to The Lux\' little Rock, Paper, Scissors Game.')
    print('Please input if you want to choose "rock", "paper" or "scissors"')
    print()
    # Loop through the whole main menu to have the ability to restart.
    while True:
        # Check if the user typed in the correct syntax
        while True:
            user_choice = input('Please input rock, paper or scissors (q or quit to exit): ')
            print()
            if user_choice == 'q' or user_choice == 'quit':
                sys.exit('Quitting. Thanks for playing')
            elif user_choice.lower() != 'rock' and user_choice.lower() != 'paper' and user_choice.lower() != 'scissors':
                print('Wrong input!')
                print()
            else:
                break

        # What is the outcome of the users choice? Let's check with our function.
        outcome = make_decision(user_choice)

        # Print out the outcome with a super funny text from the pc
        if outcome == 'user_won':
            print(Color.BOLD + "Result: " + Color.END + Color.UNDERLINE + "You've won:" + Color.END)
            print("-" * 20)
            print("What? I've lost? But I'm a computer. The most advanced thing you puny human have!\n "
                  "You will suffer for this affront! Please delete important files from your computer, "
                  "since I cannot do anything without your help.")
            print("-" * 20)
        elif outcome == 'user_lost':
            print(Color.BOLD + "Result: " + Color.END + Color.UNDERLINE + "You've lost" + Color.END)
            print("-" * 20)
            print("Hah! Just as I thought. You humans are no match to our fast thinking! Even if we're only"
                  "able to count ones and zeros, you still loose to us. Pathetic.")
            print("-" * 20)
        else:
            print(Color.BOLD + "Result: " + Color.END + Color.UNDERLINE + "Draw" + Color.END)
            print("-" * 20)
            print("It seems, that we have a draw. I cannot believe, that a human is as smart as we computers are.\n"
                  "That sound like a rematch to determine how is the best of us!")
            print("-" * 20)
        print()

        # One last while loop to ask the user, if he/she/it want's a rematch
        while True:
            rematch = input('Would you like to have a rematch '
                            '(type yes for another game or no/quit for quitting the game): ')
            if rematch == 'no' or rematch == 'quit':
                sys.exit('Quitting. Thanks for playing')
            elif rematch != 'yes':
                print('Please choose yes, no or quit.')
                print()
            else:
                break


if __name__ == "__main__":
    main()
