import turtle
import random as rand
wn = turtle.Screen()
maze_turtle = turtle.Turtle()

num_walls = 25
path_width = 10
pen_color = "black"

maze_turtle.pencolor(pen_color)
length = path_width-5  # define it before loop
maze_turtle.left(90)
for i in range(num_walls):
    door = rand.randint(path_width*2, (wall_len - path_width*2))
    barrier = rand.randint(path_width*2, (wall_len - path_width*2))
    maze_turtle.forward(10)
    maze_turtle.penup()
    maze_turtle.forward(path_width*2)
    maze_turtle.pendown()
    maze_turtle.forward(length)
    maze_turtle.left(90)
    length += path_width
    if i > 4:
        maze_turtle.forward(40)
        maze_turtle.left(90)
        maze_turtle.forward(path_width*2)
        maze_turtle.back(path_width*2)
        maze_turtle.right(90)
    
    

wn.mainloop()
# python3 -m py_compile /Users/evanpaul/VSCodeProjects/1.2.4_Turtle_Escape/a124_maze_spiral.py