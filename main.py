from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
pos = 0
snake_body = []
for i in range(3):
    tim = Turtle(shape="square")
    snake_body.append(tim)
    tim.color("white")
    tim.speed(0)
    tim.penup()
    tim.setpos(x=pos, y=0)
    pos -= 20
screen.update()

while True:
    screen.update()
    time.sleep(0.1)
    for body_num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[body_num - 1].xcor()
        new_y = snake_body[body_num - 1].ycor()
        snake_body[body_num].goto(new_x, new_y)

    snake_body[0].fd(20)
    snake_body[0].left(90)



screen.exitonclick()
