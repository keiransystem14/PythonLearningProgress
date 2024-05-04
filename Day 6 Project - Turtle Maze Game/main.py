import turtle
import maze

# Turtle starts moving in one path way.


def create_obstacles():

    obstacle_square = turtle.Turtle()
    obstacle_square.penup()
    obstacle_square.goto(-60, 70)
    obstacle_square.pendown()
    obstacle_square.shape("square")
    obstacle_square.shapesize(3, 3, 1)
    obstacle_square.color("#800000")
    obstacle_square.width(8)
    obstacle_square.left(90)

    # Create Triangle Obstacle
    obstacle_triangle = turtle.Turtle()
    obstacle_triangle.penup()
    obstacle_triangle.goto(240, -120)
    obstacle_triangle.pendown()
    obstacle_triangle.shape("triangle")
    obstacle_triangle.shapesize(4, 4, 1)
    obstacle_triangle.color("#FF00FF")
    obstacle_triangle.width(8)
    obstacle_triangle.left(90)

    # Create Circle Obstacle

    obstacle_circle = turtle.Turtle()
    obstacle_circle.penup()
    obstacle_circle.goto(240, 260)
    obstacle_circle.pendown()
    obstacle_circle.shape("circle")
    obstacle_circle.shapesize(4, 4, 1)
    obstacle_circle.color("#7FFFD4")
    obstacle_circle.width(8)
    obstacle_circle.left(90)

    # Return the obstacles in a list form.

    return [obstacle_square, obstacle_circle, obstacle_triangle]


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

# Gather the current position of turtle. It then updates the next position by 10 assuming that the turtle moving forward 10 places.

obstacles = create_obstacles()


def will_hit_obstacle(turtle_figure, obstacle):
    next_pos = turtle_figure.position()
    next_pos = (next_pos[0] + 70, next_pos[1])
    for obstacle in obstacles:
        if turtle_figure.distance(obstacle) < 70:
            return True
    return False


def move_turtle():

    turtle_figure.forward(70)
    turtle_figure.right(90)
    turtle_figure.forward(140)
    turtle_figure.left(90)

    while True:

        if will_hit_obstacle(turtle_figure, create_obstacles):
            turtle_figure.left(90)
            turtle_figure.forward(10)

        else:
            turtle_figure.forward(10)

        if turtle_figure.xcor() > 240:
            break


move_turtle()
turtle.done()
