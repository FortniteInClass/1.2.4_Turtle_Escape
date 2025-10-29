import turtle
import random as rand
import time

wn = turtle.Screen()
maze_turtle = turtle.Turtle()
maze_turtle.speed("fastest")

num_walls = 20
path_width = 15
maze_turtle.pencolor("black")
maze_turtle.left(90)


def draw_door(distance):
    '''Draw a door by lifting pen'''
    maze_turtle.forward(distance)
    maze_turtle.penup()
    maze_turtle.forward(path_width)
    maze_turtle.pendown()

def draw_barrier(distance):
    '''Draw a barrier by drawing a perpendicular line'''
    maze_turtle.forward(distance)
    maze_turtle.left(90)
    maze_turtle.forward(path_width * 2)
    maze_turtle.back(path_width * 2)
    maze_turtle.right(90)

# draw maze
length = path_width
for i in range(num_walls):
    wall_len = length
    if i == 0 or i == num_walls - 1:
        maze_turtle.forward(wall_len)
    elif wall_len > path_width * 4:
        door = rand.randint(path_width * 2, wall_len - path_width * 2)
        barrier = rand.randint(path_width * 2, wall_len - path_width * 2)
        while abs(door - barrier) < path_width:
            door = rand.randint(path_width * 2, wall_len - path_width * 2)
            barrier = rand.randint(path_width * 2, wall_len - path_width * 2)

        if door < barrier:
            draw_door(door)
            draw_barrier(barrier - door - path_width)
            maze_turtle.forward(wall_len - barrier)
        else:
            draw_barrier(barrier)
            draw_door(door - barrier)
            maze_turtle.forward(wall_len - door - path_width)
    else:
        maze_turtle.forward(wall_len)

    maze_turtle.left(90)
    length += path_width

maze_turtle.hideturtle()

maze_runner = turtle.Turtle(shape="turtle")
maze_runner.color("blue")
maze_runner.penup()
maze_runner.speed(1)
start_x = -path_width * 2
start_y = -path_width * 2
maze_runner.goto(start_x, start_y)
maze_runner.pendown()

hud = turtle.Turtle()
hud.hideturtle()
hud.penup()
hud.color("purple")
hud.goto(-length * 0.6, length * 0.7)

amount = 10
game_active = False
start_time = 0.0

def update_hud(message=""):
    """Update HUD with time and message"""
    hud.clear()
    if game_active:
        timespent = time.time() - start_time
        hud.write(f"Time: {timespent:.2f}s\n{message}", font=("Arial", 14, "bold"))
    else:
        hud.write(message, font=("Arial", 14, "bold"))

def reset_game():
    """Restart maze runner position and timer"""
    global start_time, game_active
    maze_runner.penup()
    maze_runner.goto(start_x, start_y)
    maze_runner.setheading(0)
    maze_runner.pendown()
    start_time = time.time()
    game_active = True
    update_hud("Game started. Press arrow keys to aim and G to move")

def check_escape():
    """Check if turtle escaped the maze"""
    global game_active
    if maze_runner.xcor() > length-120 or maze_runner.ycor() > length-120:
        timespent = time.time() - start_time
        game_active = False
        update_hud(f"Escaped in {timespent:.2f} seconds.\nPress R to restart.")

def move_runner():
    """Move turtle if game active"""
    if not game_active:
        update_hud("Press R to start game")
        return
    maze_runner.forward(amount)
    update_hud()  
    check_escape()

def go_up():
    maze_runner.setheading(90)
def go_down():
    maze_runner.setheading(270)
def go_left():
    maze_runner.setheading(180)
def go_right():
    maze_runner.setheading(0)

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(move_runner, "g")
wn.onkeypress(reset_game, "r")
wn.listen()

update_hud("Press R to start. Use arrows + G to move")
wn.mainloop()

#Conclusion Questions 

'''1) Pseudocode was useful to visualize and figure out how to structure the functions before coding them. It helped me break down the problem into smaller parts and made the coding process smoother.'''
'''2) The draw_door function works by moving the turtle forward a specified distance, then lifting the pen to create a gap (the door) before continuing forward. The draw_barrier function creates a barrier by moving forward, turning left to draw a perpendicular line, and then returning to the original direction. Both functions work together in the maze drawing loop to create openings and barriers in the maze.'''