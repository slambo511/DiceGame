# imports always go at the top of the file and are there to provide the functions this program
# needs.

import csv
import random


# 1.Allows  two  players  to  enter  their  details,  which  are  then  authenticated  to  
# ensure  that  they  are authorised players.

# Class to hold information about the users
class user:
    def __init__(self, user_name, user_pw, is_valid, points):
        self.user_name = user_name
        self.user_pw = user_pw
        self.is_valid = is_valid
        self.points = points

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
            print("Login successful player " + user_no + "\n")
            user_info.is_valid = True
            return
        else:
            print("Login unsuccessful player " + user_no + "\n")
    print("Too many log in attempts... game exiting...")
    quit(0)


# Create two user objects with no information as placeholders for the login_attempts function
player1 = user("", "", False, 0)
player2 = user("", "", False, 0)


# Call the login_attempts function twice for both players
login_attempts(player1, "one")
login_attempts(player2, "two")

# Criteria 1 met.

# 2.Allows each player to roll two 6-sided dice.

# Create a class to represent a die, the player can determine the number of sides, so this
# class can be re-used for different programs
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

# 3.Calculates and outputs the points for each round and each player’s total score.

# The rules are:
#	 •The points rolled on each player’s dice are added to their score.
#    •If the total is an even number, an additional 10 points are added to their score.
#  	 •If the total is an odd number, 5 points are subtracted from their score.
#	 •If they roll a double, they get to roll one extra die and get the number of points 
#	  rolled added to their score.
#	 •The score of a player cannot go below 0 at any point.
#	 •The person with the highest score at the end of the 5 rounds wins.
#	 •If  both  players  have  the  same  score  at  the  end  of  the  5  rounds,  they  
#	  each  roll  1  die  and whoever gets the highest score wins (this repeats until 
#	  someone wins).

def play_game(player_one, player_two):
    dice_one = Die(6)
    dice_two = Die(6)
    input("Player one, press enter to roll your dice...\n")
    p1_roll_one = dice_one.roll()
    p1_roll_two = dice_two.roll()
    p1_roll_total = p1_roll_one + p1_roll_two
    print("You rolled a " + str(p1_roll_one) + " and a " + str(p1_roll_two) + 
          " totalling " + str(p1_roll_total) + "\n")
    input("Player two, press enter to roll your dice...\n")
    p2_roll_one = dice_one.roll()
    p2_roll_two = dice_two.roll()
    p2_roll_total = p2_roll_one + p2_roll_two
    print("You rolled a " + str(p2_roll_one) + " and a " + str(p2_roll_two) +
          " totalling " + str(p2_roll_total) + "\n")

    
play_game(player1, player2)