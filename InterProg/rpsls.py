# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock"
# to numbers as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'Rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'Paper':
        return 2
    elif name == 'Lizard':
        return 3
    elif name == 'Scissors':
        return 4
    else:
        print 'Sorry, not an available weapon.'

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return 'Rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'Paper'
    elif number == 3:
        return 'Lizard'
    elif number == 4:
        return 'Scissors'
    else:
        print 'Range Error'

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ''
    # print out the message for the player's choice
    print 'Player chooses ' + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice
    # compute difference of comp_number and player_number modulo five
    winner = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if winner == 0:
        print 'Player and Computer Tie...'
    elif winner == 3 or winner == 4:
        print 'Drat! Player Wins!'
    elif winner == 1 or winner == 2:
        print 'Bazinga! Computer Wins!'


print ''
print '***** Rock, Paper, Scissors, Lizard, Spock *****'
print ''
print 'Hello! What is your name?'
user = raw_input('> ' )
print ''

print 'Well, ' + user + ', do you dare challenge me?'
game = raw_input('> ').lower()

if game == 'yes' or game == 'y':
    player_choice = raw_input('Choose Weapon: ').title()
    rpsls(player_choice)
    
elif game == 'no' or game == 'n':
    print 'Goodbye.'
    print ''

else:
    print "I'm sorry, I don't understand that."
    print ''
