import turtle
import random


screen = turtle.Screen()
screen.title("Color generator")
screen.bgcolor("black")


t = turtle.Turtle()
t.speed(0)
t.penup()


def draw_cyan_dot():
    t.color("cyan")
    t.dot(5)


def move_and_erase(x, y):
    t.clear()  
    t.goto(x, y)  
    draw_cyan_dot()  


draw_cyan_dot()

screen.onclick(move_and_erase)

turtle.mainloop()
