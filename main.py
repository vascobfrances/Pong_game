from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen= Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")

screen.onkeypress(r_paddle.go_up_continuous, "Up")
screen.onkeypress(r_paddle.go_down_continuous, "Down")
screen.onkeypress(l_paddle.go_up_continuous, "w")
screen.onkeypress(l_paddle.go_down_continuous, "s")
screen.onkeyrelease(r_paddle.stop_paddle, "Up")
screen.onkeyrelease(r_paddle.stop_paddle, "Down")
screen.onkeyrelease(l_paddle.stop_paddle, "w")
screen.onkeyrelease(l_paddle.stop_paddle, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    r_paddle.move()
    l_paddle.move()
    ball.move()

    if ball.ycor() > 285  or ball.ycor() < -285: #verificar colisões com parede sup e inf
        ball.bounce_y()

    if ball.xcor() > 390: #verificar colisões com parede dto
        scoreboard.r_point()
        ball.reset_position()

    if ball.xcor() < -390:  # verificar colisões com parede esq
        scoreboard.l_point()
        ball.reset_position()

    #verificar colisão com paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

screen.exitonclick()
