import turtle
import maze

# Create the Turtle figure
turtle_figure = turtle.Turtle()
turtle_figure.penup()
turtle_figure.goto(80, -250)
turtle_figure.pendown()
turtle_figure.shape("turtle")
turtle_figure.shapesize(2, 2, 1)
turtle_figure.color("#008000")
turtle_figure.width(8)
turtle_figure.left(90)

# Move
turtle_figure.forward(70)
turtle_figure.right(90)


turtle.mainloop()
