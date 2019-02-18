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

# function to handle the points system detailed above
# works by accepting the two dice rolls made by the player checking if the total is a mod
# of 2 (even) and amending the player points accordingly. It also handles the case if a
# double is rolled by rolling another die and adding the score on. Lastly it ensures the
# player's score does no go below zero.
def score_handler(player_info, dice_one, dice_two):
    player_info.points += dice_one
    player_info.points += dice_two
    if (dice_one + dice_two) % 2 == 0:
        player_info.points += 10
    else:
        player_info.points -= 5
    if dice_one == dice_two:
        input("You rolled a double, so you get another roll, click enter to roll\n")
        extra_die = Die(6)
        extra_roll = extra_die.roll()
        input("You rolled a " + str(extra_roll) + ", press enter to continue\n")
        player_info.points += extra_roll
    if player_info.points < 0:
        player_info.points = 0

# function to handle the game mechanics and reporting the scores to the players
# Creates to dice and uses them one player after another. Passes the dice rolls
# to the score_handler function.
def play_game(player_one, player_two):
    dice_one = Die(6)
    dice_two = Die(6)
    input("Player one, press enter to roll your dice...\n")
    p1_roll_one = dice_one.roll()
    p1_roll_two = dice_two.roll()
    p1_roll_total = p1_roll_one + p1_roll_two
    print("You rolled a " + str(p1_roll_one) + " and a " + str(p1_roll_two) + 
          " totalling " + str(p1_roll_total) + "\n")
    score_handler(player_one, p1_roll_one, p1_roll_two)
    print("Player one, your score is now " + str(player_one.points))
    input("Player two, press enter to roll your dice...\n")
    p2_roll_one = dice_one.roll()
    p2_roll_two = dice_two.roll()
    p2_roll_total = p2_roll_one + p2_roll_two
    print("You rolled a " + str(p2_roll_one) + " and a " + str(p2_roll_two) +
          " totalling " + str(p2_roll_total) + "\n")
    score_handler(player_two, p2_roll_one, p2_roll_two)
    print("Player two, your score is now " + str(player_two.points))

# 4.Allows the players to play 5 rounds.

# simple for loop which playes 5 rounds, code can easily be amended to alter
# the number of rounds if necessary.
for i in range (1, 6):
    print("Round " + str(i))
    play_game(player1, player2)

# 5.If  both  players  have  the  same  score  after  5  rounds,  allows  each  player  to  roll  
# 1  die  each  until  someone wins.

# function which handles a single die roll for both players in the event of a tied score after
# the final round.
def tie_roll():
    draw_dice = Die(6)
    input("\nPlayer one, press enter to roll...")
    p1_tie_roll = draw_dice.roll()
    input("\nPlayer one, press enter to roll...")
    p2_tie_roll = draw_dice.roll()
    return p1_tie_roll, p2_tie_roll


# 6.Outputs who has won at the end of the 5 rounds.

# function which handles tie_breaks using a boolen to check if the tie has been resolved, then
# calls the tie_roll() function to try and break the tie.
def tie_breaker():
    tie_resolved = False
    # draw_dice = Die(6)

    while tie_resolved == False:
        p1_roll, p2_roll = tie_roll()
        print("Player one rolled a " + str(p1_roll) + ", player two rolled a " + str(p2_roll))
        if p1_roll > p2_roll:
            tie_resolved = True
            return("Player 1")
        elif p1_roll < p2_roll:
            tie_resolved = True
            return("Player 2")
        else:
            print("Another Tie!")
       

# simple if, elif, else loop to ascertain the winner, calling the tie_breaker() function if
# necessary.
if player1.points > player2.points:
    print("Player one wins!")
    winner = "Player 1"
elif player1.points < player2.points:
    print("Player two wins!")
    winner="Player 2"
else:
    print("Draw, roll again")
    winner = tie_breaker()
    print(winner + " wins the tie break and the game!!!")


# 7.Stores the winner’s score, and their name, in an external file.

# asks the winner for their name using input validation to ensure somehting is entered
# then checks whether they are player 1 or 2, then adds their username and score to the 
# information - placing all 3 pieces into the Winners.csv file
winner_name = input("\n" + winner + " enter your name for the hall of fame: ")
print("\n")
if winner_name == "":
    print("You cannot enter a blank name. Using name \"winner\" instead")
    winner_name = "winner"
if winner == "Player 1":
    winner_username = player1.user_name
    winner_score = player1.points
else:
    winner_username = player2.user_name
    winner_score = player2.points

with open("Winners.csv", mode='a', newline='') as winner_file:
    winner_writer = csv.writer(winner_file, delimiter = ',')
    winner_writer.writerow([winner_username, winner_name, str(winner_score)])


# 8.Displays the score and player name of the top 5 winning scores from the external file

# works by opening the Winners.csv file and readin the contents into a list. The code
# then sorts the list by score descending from highest to lowest. Finally it uses a
# for loop to list the top 5 players by score.
with open("Winners.csv", 'r') as winners_list:
    winner_reader = csv.reader(winners_list)
    winner_list = list(winner_reader)

sorted_winners = sorted(winner_list, key=lambda x: int(x[2]), reverse=True)

print("Top 5 players so far...\n")
for i in range(0,5):
    print(str(i+1) + " " + sorted_winners[i][1] + " " + 
          sorted_winners[i][2] + " (username - " + sorted_winners[i][0] + ")")
print("\n")

# All 8 of the requirements are met and the rules are applied as specified.
# Next testing will happen to ensure nothing unexpected happens.