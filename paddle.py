from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_direction = 0
        self.move_speed = 20

    # def go_up(self):
    #     new_y = self.ycor() + 20
    #     self.goto(self.xcor(), new_y)
    #
    # def go_down(self):
    #     new_y = self.ycor() - 20
    #     self.goto(self.xcor(), new_y)

    def go_up_continuous(self):
        self.move_direction = 1

    def go_down_continuous(self):
        self.move_direction = -1

    def stop_paddle(self):
        self.move_direction = 0

    def move(self):
        new_y = self.ycor() + self.move_speed * self.move_direction
        self.goto(self.xcor(), new_y)