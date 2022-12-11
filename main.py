import turtle as t
from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

# tim.shape("")
tim.color("red")
t.colormode(255)
b= True
tim.speed(0)
for _ in range(1, 73):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.circle(50)
    tim.setheading(tim.heading()+5)









# st = [0, 90, 180, 270]
# t.colormode(255)
# tim.pensize(5)
# def walk(kolor, dlugosc):
#     tim.color(random.randint(0,255),random.randint(0,255), random.randint(0,255))
#     tim.forward(15)
#     tim.setheading(dlugosc)
# a=  True
# while a:
#     kolor = tim.color(random.randint(0,255),random.randint(0,255), random.randint(0,255))
#     dlugosc = random.choice(st)
#     walk(kolor, dlugosc)
#












# a = 360
# b = 3
# d = 0
# while d != 9:
#     # paint()
#     for _ in range(b):
#         tim.forward(100)
#         tim.right(a/b)
#     b += 1
#     d += 1
#     tim.pencolor(random.choice(color))










# for game in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)




# while b:
#     timm_the_turtle.color("red")
#     timm_the_turtle.forward(a)
#     timm_the_turtle.right(90)
#     a += 5
#     timm_the_turtle.color("yellow")
#     timm_the_turtle.forward(a)
#     timm_the_turtle.right(90)
#
#     timm_the_turtle.color("blue")
#     timm_the_turtle.forward(a)
#     timm_the_turtle.right(90)
#     a += 5
#     timm_the_turtle.color("green")
#     timm_the_turtle.forward(a)
#     timm_the_turtle.right(90)



















screen = Screen()
screen.exitonclick()