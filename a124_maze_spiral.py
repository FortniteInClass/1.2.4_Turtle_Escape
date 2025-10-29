import turtle
import random as rand

wn = turtle.Screen()
maze_turtle = turtle.Turtle()
maze_turtle.speed("fastest")  

num_walls = 25      
path_width = 10      
pen_color = "black"
maze_turtle.pencolor(pen_color)

maze_turtle.left(90)


def draw_door(distance):
    """Draw a door in the maze wall"""
    maze_turtle.forward(distance)
    maze_turtle.penup()
    maze_turtle.forward(path_width)
    maze_turtle.pendown()

def draw_barrier(distance):
    """Draw a barrier in the path"""
    maze_turtle.forward(distance)
    maze_turtle.left(90)
    maze_turtle.forward(path_width * 2)
    maze_turtle.back(path_width * 2)
    maze_turtle.right(90)


length = path_width

for i in range(num_walls):
    wall_len = length

    if wall_len > path_width * 4:
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


# create maze runner
maze_runner = turtle.Turtle(shape="turtle")  # you can try "circle", "arrow", etc.
maze_runner.color("blue")
maze_runner.penup()


maze_runner.setheading(0)
maze_runner.goto(-path_width * 2, -path_width * 2)
maze_runner.pendown()


def go_up():
    '''Turn maze runner to face up direction.'''
    maze_runner.setheading(90)

def go_down():
    '''Turn maze runner to face down direction.'''
    maze_runner.setheading(270)

def go_left():
    '''Turn maze runner to face left direction.'''
    maze_runner.setheading(180)

def go_right():
    '''Turn maze runner to face right direction.'''
    maze_runner.setheading(0)

amount = 10

def move_runner():
    """move maze runner forward by amount"""
    maze_runner.forward(amount)

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(move_runner, "g")   
wn.listen()

wn.mainloop()
