# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user38_GK5tHWhuv1S8bK4.py

import simplegui

# define global variables
current_time = 0
running = False
total_stops = 0
win_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t / 600
    b = t % 600 / 100
    c = t % 600 % 100 / 10
    d = t % 600 % 100 % 10
    return str(a) + ':' + str(b) + str(c) + '.' + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    start_button
    timer.start()
    running = True
  
def stop():
    global running, total_stops, current_time, win_stops
    stop_button
    timer.stop()
    if running:
        total_stops += 1
        if int(format(current_time)[-1]) == 0:
            win_stops += 1
    running = False

def reset():
    global current_time, total_stops, win_stops, running
    reset_button
    timer.stop()
    current_time = 0
    total_stops = 0
    win_stops = 0
    running = False
    

# define event handler for timer with 0.1 sec interval
def timer():
    global current_time
    current_time += 1

# define draw handler
def draw_handler(canvas):
    global current_time
    time = format(current_time)
    canvas.draw_text(time, (70, 180), 60, 'White')
    canvas.draw_text(str(win_stops), (200, 25), 30, 'Lime')
    canvas.draw_text(' / ', (225, 25), 30, 'White')
    canvas.draw_text(str(total_stops), (245, 25), 30, 'Red')
    
# create frame
f = simplegui.create_frame('Stop Watch Game', 300, 300)

# register event handlers
start_button = f.add_button('Start', start, 100)
stop_button = f.add_button('Stop', stop, 100)
reset_button = f.add_button('Reset', reset, 100)
f.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer)

# start frame
f.start()
