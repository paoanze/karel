from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    move_to_beeper()
    if beepers_present():
        pick_beeper()
    return_to_starting_point()
    
def move_to_beeper():
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def return_to_starting_point():
    turn_left()
    turn_left()
    move()
    move()    
    move()
    turn_right()
    move()
    turn_right()
    
    
    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()