# World of Python Discord Server Challenge - Count Integers
import sys


def main():
    #Create a list to save the entered numbers
    user_input=[]

    #Greet the Player and give a little info
    print("Welcome to The_Lux' little \"Count Integers\" script")
    print("To quit this program enter 'q' instead of a number.")
    
    for i in range(10):
        #Ask user for numbers, convert them to Integers and append them to the list
        #user_input.append(int(input('Please input your ' + str(i+1) + '. number: ' )))
        while True:
            entered_number = input('Please input your ' + str(i+1) + '. number: ')
            if entered_number == 'q':
                sys.exit("Good bye")
            else:
                try:
                    user_input.append(int(entered_number))
                    break
                except:
                    print("Please type in a number")

    #Show every number with a + sign and print the summary of them
    print('+'.join(map(str, user_input)) + "=" + str(sum(user_input)))


if __name__ == "__main__":
    main()
