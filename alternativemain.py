from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)

guess = screen.textinput("Make your bet", "Who will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_y = -150
turtles = []

for color in colors:
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    turtle.speed("slow")
    turtle.penup()
    turtle.goto(-280, start_y)
    start_y += 50
    turtles.append(turtle)

game_on = True
while game_on:
    for turtle in turtles:
        turtle.speed("slowest")
        turtle.forward(random.randint(1, 50))
        if turtle.xcor() >= 250:
            game_on = False
            print(f"{turtle.pencolor().capitalize()} wins!")
            if guess == turtle.pencolor(): print("You win!")
            else:
                print("You lose!")
            break

screen.exitonclick()
