# This code is an algorythm for Reeborg's world Hurles 1-4

# Paste the code in this link https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json




def turn_right():
    # there is no built in turn_right so I made one
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    # there is no built in turn_right so I made one
    turn_left()
    turn_left()


def jump():
    # this jumps over the hurdle and faces right when done
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while at_goal() == False:
    if wall_in_front() == True and is_facing_north() == False :
        # 'and is_facing_north() == False' prevents Reeborg from facing the top wall and infinitely moving left
        turn_left()
    elif wall_on_right() == True:
        move()
        #climbs the wall
    elif wall_on_right() == False:
        turn_right()
        move()
        turn_right()
        # once at the top this positions Reeborg to go to the right of the wall and prepare for descent
      
        while wall_in_front() == False:
            move()
            # keeps on moveing right when there are no walls in the way
        turn_left()
        #once Reeborg hits the ground he will turn to face right
    else:
        move()