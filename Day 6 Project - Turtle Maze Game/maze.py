import turtle

screen = turtle.Screen()
screen.tracer(0)

# The width of the boxes

turtle_maze_width = 200

turtle_maze = turtle.Turtle()


# Maze color border

turtle_maze.width(8)
turtle_maze.hideturtle()

turtle_maze.speed(0)

# Creates the size of the maze

turtle_maze.penup()
turtle_maze.goto(-turtle_maze_width, 350)


# Draw's the Maze


def draw_turtle_maze(color):

    # Draw the outter boxes

    turtle_maze.color(color)
    turtle_maze.pendown()
    turtle_maze.forward(turtle_maze_width)
    turtle_maze.penup()
    turtle_maze.forward(180)
    turtle_maze.pendown()
    turtle_maze.forward(turtle_maze_width)
    turtle_maze.right(90)
    turtle_maze.forward(180)
    turtle_maze.right(90)
    turtle_maze.forward(turtle_maze_width)
    turtle_maze.penup()
    turtle_maze.forward(180)
    turtle_maze.pendown()
    turtle_maze.forward(turtle_maze_width)
    turtle_maze.right(90)
    turtle_maze.forward(180)
    turtle_maze.right(90)
    turtle_maze_x, turtle_maze_y = turtle_maze.pos()
    turtle_maze.penup()

    # Position of middle line in all boxes

    turtle_maze.goto(turtle_maze_x, turtle_maze_y - 90)

    # Draw the inner lines inside the boxes

    turtle_maze.pendown()
    turtle_maze.forward(100)
    turtle_maze.penup()
    turtle_maze.forward(90)
    turtle_maze.pendown()
    turtle_maze.forward(200)
    turtle_maze.penup()
    turtle_maze.forward(100)
    turtle_maze.pendown()
    turtle_maze.forward(90)
    turtle_maze.penup()

    # Gap between each box

    turtle_maze.goto(turtle_maze_x, turtle_maze_y - 190)


# The color of each box in the Maze

for color in ["#000000", "#FFA500", "#808000"]:
    draw_turtle_maze(color)

screen.tracer(1)
