#pong game 

import turtle
from time import sleep
# setting the screen
win = turtle.Screen()
win.title("pong game")
win.bgcolor("blue")
win.setup(width=700, height=430)
win.tracer(0)

class Sushobhan(turtle.Turtle):#this class is to define and set values of all the turtle objects 
    def __init__(self, width, length, x, y):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=width,stretch_len=length)
        self.penup()
        self.goto(x, y)

Paddle_A = Sushobhan(5, 0.5, -270, 0)
Paddle_B = Sushobhan(5, 0.5, 270, 0)
ball = Sushobhan(0.6, 0.6, 0, 0)
line1 = Sushobhan(0.05, 28, 0, 190)
line2 = Sushobhan(0.05, 28, 0, -190)
ball.shape("circle")
ball.color("red")
ball.dx = 3
ball.dy = 3

# Pen for Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 18, "normal"))

# moving the paddles  
def move_paddle(h):
    if h==1:
        y = Paddle_A.ycor()
        y += 20
        Paddle_A.sety(y) 
    elif h==2:
        y = Paddle_A.ycor()
        y -= 20
        Paddle_A.sety(y)
    elif h==3:
        y = Paddle_B.ycor()
        y += 20
        Paddle_B.sety(y)
    else:
        y = Paddle_B.ycor()
        y -= 20
        Paddle_B.sety(y)

#to move the left paddle press 'z' and 'x' and for the right paddle, use 'right' and 'left' key
win.listen()
win.onkeypress(lambda: move_paddle(1), "x")
win.onkeypress(lambda: move_paddle(2), "z")
win.onkeypress(lambda: move_paddle(3), "Right")
win.onkeypress(lambda: move_paddle(4), "Left")

Score_A = 0
Score_B = 0
while True:
    win.update()
    sleep(0.01)
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border checking

    # Top and bottom
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1
    
    elif ball.ycor() < -190:
        ball.sety(-190)
        ball.dy *= -1
    #right and left side
    if ball.xcor() > 290:
        Score_A+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Score_A, Score_B), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -290:
        Score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Score_A, Score_B), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    
        # Paddle and ball collisions
    elif ball.xcor() < -264 and ball.ycor() < Paddle_A.ycor() + 50 and ball.ycor() > Paddle_A.ycor() - 50 and ball.xcor() > -270:
        ball.dx *= -1 
    
    elif ball.xcor() > 264 and ball.ycor() < Paddle_B.ycor() + 50 and ball.ycor() > Paddle_B.ycor() - 50 and ball.xcor() < 270:
        ball.dx *= -1

    
#Sushobhan Mahato