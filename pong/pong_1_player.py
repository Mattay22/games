import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @Mattay22")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)


###score

score_a = 0
score_b = 0

###difficulty
ballx = (ball.dx = 0.1)
bally = (ball.dy = 0.1)


#padle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("triangle")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a._rotate(180)


#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ballx = {}
bally = {}

###pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("legend: 0", align="center", font=("Courier", 24, "normal"))



#function a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#  # Keyboard binding    A                  
wn.listen()
wn.onkeypress(paddle_a_up, "w")            
wn.listen()
wn.onkeypress(paddle_a_down, "s")


###main game loop

while True:
    wn.update()

    ##move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ###border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 350:
        ball.setx(350)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        ballx += 0.1
        bally += 0.1
        pen.clear()
        pen.write("Legend: {}".format(score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1


