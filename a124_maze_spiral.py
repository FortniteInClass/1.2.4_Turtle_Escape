import turtle

wn = turtle.Screen()
maze_turtle = turtle.Turtle()

num_walls = 25
path_width = 10
pen_color = "black"

maze_turtle.pencolor(pen_color)
length = path_width  # define it before loop
maze_turtle.left(90)
for i in range(num_walls):
    maze_turtle.forward(length)
    maze_turtle.left(90)
    length += path_width

wn.mainloop()
# python3 -m py_compile /Users/evanpaul/VSCodeProjects/1.2.4_Turtle_Escape/a124_maze_spiral.py
