# implementation of the card game - Memory

import simplegui
import random

#global variables
state = 0
turns = 0
deck = [card for card in range(1, 9)]*2
exposed = [False]*16
card1 = 0
card2 = 0
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png") 

# helper function to initialize globals
def new_game():
    global state, turns, card1, card2, deck, exposed
    state = 0
    turns = 0
    random.shuffle(deck)
    exposed = [False]*16
    card1 = 0
    card2 = 0
   
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns, card1, card2
    selection = pos[0] // 50 # single row of cards means I only care about the x coordinate
    
    if not exposed[selection]: # if card is not already visible
        if state == 0: # new game
            card1 = selection
            exposed[selection] = True
            state = 1
        elif state == 1: # 1 card turned over
            card2 = selection
            exposed[selection] = True
            state = 2
            turns += 1
        else: # 2 cards turned over
            exposed[selection] = True
            if deck[card1] != deck[card2]: # cards do not match
                exposed[card1] = False
                exposed[card2] = False
            card1 = selection # both old cards will turn over when new card is selected
            state = 1
                       
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card in range(len(deck)):
        if exposed[card]: # draw card 'front' aka number
            canvas.draw_polygon([[card*50, 0], [(card + 1)*50, 0], [(card + 1)*50, 100], [card*50, 100]], 1, 'Blue', 'White')
            canvas.draw_text(str(deck[card]), [card*50 + 6, 75], 75, 'Blue')
        else: # draw card back
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (card*50 + 25, 50),(50, 100))
    label.set_text('Turns = ' + str(turns))  

# create frame and add a button and labels
frame = simplegui.create_frame('Memory', 800, 100)
frame.set_canvas_background('Green')
frame.add_button('Reset', new_game)
label = frame.add_label('Turns = ' + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
