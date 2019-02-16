# imports always go at the top of the file and are there to provide the functions this program
# needs.

import csv
import random


# Class to hold information about the users
class user:
    def __init__(self, user_name, user_pw, is_valid):
        self.user_name = user_name
        self.user_pw = user_pw
        self.is_valid = is_valid

# 1.Allows  two  players  to  enter  their  details,  which  are  then  authenticated  to  
# ensure  that  they  are authorised players.

# Function which takes the username and passwords entered and cycles throught the Users.csv
# file. If it finds a username and password that match it returns True otherwise it returns
# False. This ensures only authorised players can login.
def check_user(username, password):
    with open("Users.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for user in reader:
            if user[0] == username:
                if user[1] == password:
                    return True
        return False


# Function which handles the number of times a user can login and exits the program if the
# login attempts fail
def login_attempts(user_info, user_no):    
    for login_attempt in range (1, 4):
        print("Player " + user_no + " login attempt " + str(login_attempt))
        user_info.user_name = input("Enter your username, player " + user_no + ": ")
        user_info.user_pw = input("Enter your password: ")
        if check_user(user_info.user_name, user_info.user_pw):
            print("Login successful player " + user_no)
            user_info.is_valid = True
            return
        else:
            print("Login unsuccessful player " + user_no)
    print("Too many log in attempts... game exiting...")
    quit(0)


# Create two user objects with no information as placeholders for the login_attempts function
player1 = user("", "", False)
player2 = user("", "", False)


# Call the login_attempts function twice for both players
login_attempts(player1, "one")
login_attempts(player2, "two")

# Criteria 1 met.

# 2.Allows each player to roll two 6-sided dice.

# Create a class to represent a die
class Die:
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides

    def roll(self):
        return random.randint(1, self.no_of_sides)


# Testing a dice roll with a 6 sided die
#   test_die = Die(6)
#   roll_result = test_die.roll()
#   print("The test roll is " + str(roll_result))
# Test successful