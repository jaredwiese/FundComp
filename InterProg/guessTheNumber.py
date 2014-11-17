# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# http://www.codeskulptor.org/#user38_6XyVwQCXGr6EIDc.py

import simplegui
import random
import math

# initialize global variables used in your code here
num_range = 100
secret_number = 0
guess_remain = 7


# helper function to start and restart the game
def new_game(num_range):
    global secret_number, guess_remain
    secret_number = random.randint(1, num_range)
    guess_remain = math.ceil(math.log(num_range + 1, 2))
    # if num_range == 100:
        # guess_remain = 7
    # elif num_range == 1000:
        # guess_remain = 10
    print ''
    print 'New Game. Range is from 0 to %i' % num_range
    print 'Number of Remaining Guesses is %i' % guess_remain
    print ''

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game(num_range)
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game(num_range)
       
def input_guess(guess):
    # main game logic goes here	
    global secret_number, guess_remain
    guess_reset = guess_remain
    print 'Guess was ' + guess
    guess = int(guess)
    guess_remain -= 1
    print 'Number of Remaining Guesses is %i' % guess_remain
    
    if guess == secret_number:
        print 'Correct!'
        guess_remain = guess_reset
        new_game(num_range)
    elif guess > secret_number:   
        print 'Lower'
        print ''          
    elif guess < secret_number:
        print 'Higher'
        print ''  
    
    if guess_remain == 0:
        print 'Sorry, you ran out of guesses.'
        print 'The Secret Number was %i' % secret_number
        guess_remain = guess_reset
        new_game(num_range)

def draw_handler(canvas):
    canvas.draw_text('Guess', (40, 55), 45, 'Orange')
    canvas.draw_text('The', (60, 115), 45, 'Orange')
    canvas.draw_text('Number', (25, 170), 45, 'Orange')
    
# create frame
f = simplegui.create_frame("Guess the Number", 200, 200)
f.set_canvas_background('Aqua')

# register event handlers for control elements and start frame
f.add_button("Range 0 to 100)", range100, 200)
f.add_button("Range 0 to 1000)", range1000, 200)
f.add_input("Enter a Guess", input_guess, 200)
f.set_draw_handler(draw_handler)
f.start()

# call new_game
new_game(num_range)
