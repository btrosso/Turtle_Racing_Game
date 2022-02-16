import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def create_turtles(color_list):
    """
    This function will create all the turtles for the game, set their starting positions and colors.
    It will also append the turtle instances to a list for later use.
    :param color_list:
    :return:
    """
    y_temp = -100
    for color in color_list:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.pu()
        new_turtle.goto(x=-230, y=y_temp)
        all_turtles.append(new_turtle)
        y_temp += 50


create_turtles(colors)

if user_bet:
    is_race_on = True

while is_race_on:

    # a turtle object is actually 40x40
    # to detect the end we need to use: 250-(40/2) = 230

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 12)
        turtle.forward(random_distance)

screen.exitonclick()