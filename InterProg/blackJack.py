# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user38_2yetJZ2sRvKyD0o.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ''
score = 0
message = ''
game_deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print 'Invalid card: ', suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw_front(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                          [pos[0] + CARD_BACK_CENTER[0] + 1, 
                           pos[1] + CARD_BACK_CENTER[1] + 1], 
                          CARD_BACK_SIZE)

        
# define hand class
class Hand:
    def __init__(self):
        self.cards = [] # create Hand object

    def __str__(self):
        # return a string representation of a hand
        str_cards = 'Hand contains: '
        for card in self.cards:
            str_cards += str(card) + ' '
        return str_cards
        
    def add_card(self, card):
        self.cards.append(card) # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        aces = False
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                aces = True
        if aces and value < 12:
            value += 10
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 30 # extra spacing
            card.draw_front(canvas, pos)
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = [] # create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()    
    
    def __str__(self):
        # return a string representing the deck
        str_deck = 'Deck contains: '
        for card in self.cards:
            str_deck += str(card) + ' '
        return str_deck


#define event handlers for buttons
def deal():
    global in_play, deck, player, dealer, outcome, score, message
    if in_play:
        outcome = 'Player Forfeits.'
        score -= 1
        in_play = False
        deal()
        
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = ''
    message = 'Hit or Stand?'
    in_play = True

def hit():
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global in_play, deck, score, outcome, player, message
    outcome = ''
    if in_play:
        if player.get_value() < 22:
            player.add_card(deck.deal_card())
            if player.get_value() > 21:
                outcome = 'You Bust. Dealer Wins.'
                score -= 1
                message = 'Deal Again?' 
                in_play = False
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global in_play, dealer, player, score, outcome, dealer, message
    if in_play:
        while (dealer.get_value() < 17):
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = 'Dealer Busts! You Win!'
            score += 1
            message = 'Deal Again?'
            in_play = False
        elif player.get_value() > dealer.get_value():
            outcome = 'You Win!'
            score += 1
            message = 'Deal Again?'
            in_play = False
        elif player.get_value() == dealer.get_value(): 
            outcome = 'Tie. Dealer Wins.' # Dealer wins ties in our version
            score -= 1
            message = 'Deal Again?'
            in_play = False
        else:
            outcome = 'Dealer Wins.'
            score -= 1
            message = 'Deal Again?'
            in_play = False
   

# draw handler    
def draw(canvas):
    # card = Card('S', 'A') # Test Code
    # card.draw(canvas, [300, 300])
    
    canvas.draw_polygon([[10,10],[10,590],[590,590],[590,10]], 2, 'lime')
    canvas.draw_circle([300,-775], 900, 1, 'white', 'orange')
    canvas.draw_circle([300,-630], 750, 1, 'white', 'teal')
    canvas.draw_text('Blackjack', (60, 65), 65, 'black')
    dealer_label = canvas.draw_text('Dealer', (60, 175), 40, 'Red')
    player_label = canvas.draw_text('Player', (60, 400), 40, 'Blue')
    player_value = canvas.draw_text(str(player.get_value()), (95, 575), 40, 'Blue')
    str_message = canvas.draw_text(message, (250, 400), 35, 'white')
    str_outcome = canvas.draw_text(outcome, (250, 175), 35, 'white')
    if score > 0:
        str_score = canvas.draw_text('Score: ' + str(score), (425, 65), 40, 'Lime')
    elif score == 0:
        str_score = canvas.draw_text('Score: ' + str(score), (425, 65), 40, 'Black')
    else:
        str_score = canvas.draw_text('Score: ' + str(score), (425, 65), 40, 'Red')
    dealer.draw(canvas, [-72, 205])
    player.draw(canvas, [-72, 425])
    if in_play:
        dealer.cards[0].draw_back(canvas, [30, 205])
    else:
        dealer_value = canvas.draw_text(str(dealer.get_value()), (95, 350), 40, 'Red')

# initialization frame
frame = simplegui.create_frame('Blackjack', 600, 600)
frame.set_canvas_background('Green')

#create buttons and canvas callback
frame.add_button('Deal', deal, 200)
frame.add_button('Hit',  hit, 200)
frame.add_button('Stand', stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
