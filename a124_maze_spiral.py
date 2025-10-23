import turtle

wn = turtle.Screen()
maze_turtle = turtle.Turtle()

# Function to draw a barrier line
def draw_barrier(t, length=20):
    t.right(90)
    t.forward(length)
    t.backward(length)
    t.left(90)

for i in range(26):
    maze_turtle.forward(10)
    maze_turtle.penup()
    maze_turtle.forward(i * 10)
    maze_turtle.pendown()
    maze_turtle.left(90)

    # Draw a barrier line approximately 40 pixels past the door
    if i > 4:
        maze_turtle.penup()
        maze_turtle.forward(40)
        maze_turtle.pendown()
        draw_barrier(maze_turtle)
        maze_turtle.penup()
        maze_turtle.backward(40)
        maze_turtle.pendown()


wn.mainloop()