# Implementation of classic arcade game Pong

import simplegui, random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
ball_vel = [5, -2]
ball_pos = [WIDTH / 2, HEIGHT / 2]
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
score1 = 0
score2 = 0
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
started = False
RIGHT = True
LEFT = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# splash image
splash_info = ImageInfo([288, 208], [576, 416])
splash_image = simplegui.load_image("http://sandbox.yoyogames.com/extras/image/name/san2/587/350587/original/title_page.png")

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]
    else:
        ball_vel = [-random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]
    

# define event handlers
def new_game():
    global score1, score2, paddle1_pos, paddle2_pos
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2 
    score1 = 0
    score2 = 0
    directionInt = random.randrange(2)
    if directionInt == 0:
        direction = RIGHT
    else:
        direction = LEFT
    spawn_ball(direction)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([(WIDTH - 1) - PAD_WIDTH, 0],[(WIDTH - 1) - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        # ball_vel[0] = -ball_vel[0] # canvas test code
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score2 += 1   
    
    if ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS - PAD_WIDTH:
        # ball_vel[0] = -ball_vel[0] canvas test code
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            spawn_ball(LEFT)
            score1 += 1 
        
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1] 
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]  
    
    
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos],[HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "Lime")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "Red")
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH * 0.33, 60), 30, 'Lime')
    canvas.draw_text(str(score2), (WIDTH * 0.66, 60), 30, 'Red')
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
    
def keydown(key):
    global paddle1_vel, paddle1_pos, paddle2_vel, paddle2_pos
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 3
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -3
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -3
            
def keyup(key):
    global paddle1_vel, paddle1_pos, paddle2_vel, paddle2_pos, started
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['space']:
        if not started:
            started = True
            new_game()

def restart_handler():
    new_game()
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart_handler, 100)


# start frame
frame.start()
