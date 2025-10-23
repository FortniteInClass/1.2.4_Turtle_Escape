import turtle

wn = turtle.Screen()
maze_turtle = turtle.Turtle()

for i in range(26):
    maze_turtle.forward(i * 10)
    maze_turtle.left(90)


wn.mainloop()