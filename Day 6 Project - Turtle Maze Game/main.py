import turtle
import os
from maze import *


# Creating a Finish line track in the Turtle Maze game
def finish_line():

    black_square = turtle.Turtle()
    gap_size = 20

    # Black squares row 1
    black_square.shape("square")
    black_square.penup()
    black_square.color("black")

    # It starts the loop and will iterate it 4 times from i which takes values from 0 to 3.
    for i in range(4):
        # This means the turtle is moved into a new position. Inside the goto brackets it calculates the new position in the x-coordinates for each iteration of the loop. This means gap size doubled for each iteration.
        black_square.goto((140 - (i * gap_size * 2)), 350)
        black_square.stamp()

    # Black squares row 2
    for i in range(4):
        black_square.goto(((180 - gap_size) - (i * gap_size * 2)), 350 - gap_size)
        black_square.stamp()

    return [black_square]


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
turtle_figure.speed(1)

# Gathers the current position of the finish line.

Complete = finish_line()

# Gather the current position of turtle. It then updates the next position by 10 assuming that the turtle moving forward 10 places.

obstacles = create_obstacles()

# Creating a will_hit_obstacle function to check if the turtle is in collision with the object


def will_hit_obstacle(turtle_figure, obstacle):
    for obstacle in obstacles:

        # Check if the turtle is within the collision distance from the obstacles (Triangle, Square, Circle)

        if turtle_figure.distance(obstacle) <= 65:
            return obstacle  # It returns the obstacle object if collision  is detected
    return None  # It returns nothing if collision is not detected


# Creating reach_finish_line function to check if the turtle object has arrived at the finish line.


def reach_finish_line(turtle_figure, finish):
    for finish in Complete:
        if turtle_figure.distance(finish) <= 60:
            return finish
    return None


# The turtle moves in the maze.


def move_turtle():

    turtle_figure.forward(70)
    turtle_figure.right(90)
    turtle_figure.forward(160)
    turtle_figure.left(90)

    while True:

        # Check for obstacles and gather the obstacle object if there is a possible collision between turtle and the object.

        obstacle_hit = will_hit_obstacle(turtle_figure, obstacles)

        if obstacle_hit:
            if obstacle_hit.shape() == "triangle":
                turtle_figure.left(90)
                turtle_figure.forward(290)
                turtle_figure.right(90)
                turtle_figure.forward(100)
                turtle_figure.right(90)
                turtle_figure.forward(110)
                turtle_figure.left(90)
                turtle_figure.forward(90)
                turtle_figure.left(90)
                turtle_figure.forward(120)
                turtle_figure.right(90)
            elif obstacle_hit.shape() == "square":
                turtle_figure.right(90)
                turtle_figure.forward(290)
                turtle_figure.left(90)
                turtle_figure.forward(100)
                turtle_figure.left(90)
                turtle_figure.forward(140)
                turtle_figure.right(90)
                turtle_figure.forward(90)
                turtle_figure.right(90)
                turtle_figure.forward(145)
                turtle_figure.left(90)
            else:
                turtle_figure.left(90)
                turtle_figure.forward(290)
                turtle_figure.right(90)
                turtle_figure.forward(100)
                turtle_figure.right(90)
                turtle_figure.forward(140)
                turtle_figure.left(90)

        else:
            finish_hit = reach_finish_line(turtle_figure, Complete)
            if finish_hit:
                complete_text = turtle.Turtle()
                complete_text.penup()
                complete_text.hideturtle()
                complete_text.color("black")
                complete_text.goto(-300, -340)
                complete_text.write(
                    "Well Done!! The Turtle Completed the Maze!!!", font=("Ariel", 40)
                )
                screen.update()


move_turtle()
turtle.mainloop()
