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


#padle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("triangle")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a._rotate(180)


#padle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("triangle")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

###pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Christine: 0  legend: 0", align="center", font=("Courier", 24, "normal"))

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(50, 0)
pen1.write("", align="center", font=("Courier", 24, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(-150, -100)
pen2.write("", align="center", font=("Courier", 24, "normal"))

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

#function b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

    #  # Keyboard binding    A                  
wn.listen()
wn.onkeypress(paddle_b_up, "o")            
wn.listen()
wn.onkeypress(paddle_b_down, "k")

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
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Christine: {}  Legend: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        pen2.write("fuck ooooo", align="left", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Christine: {}  Legend: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))    
        pen1.write("well done big matty", align="left", font=("Courier", 24, "normal"))
        


    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)
        pen1.clear()
        #os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)
        pen2.clear()
        #os.system("afplay bounce.wav&")

