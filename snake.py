from turtle import Turtle



class Snake:
    def __init__(self):
        self.snake_body = []
        self.pos = 0
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            tim = Turtle(shape="square")
            self.snake_body.append(tim)
            tim.color("white")
            tim.speed(0)
            tim.penup()
            tim.setpos(x=self.pos, y=0)
            self.pos -= 20

    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)

        self.head.fd(20)


    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)


    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)








