#part 1
import turtle
import os
import math
import random
import time

#screen
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Oopie revolution")
wn.bgpic("background.gif")

###import shape
wn.register_shape("invader.gif")
wn.register_shape("gun.gif")
wn.register_shape("bullet.gif")
wn.register_shape("UNtitled.gif")

##draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

###set score
score = 0

###draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "score: %s" %score
score_pen.write(scorestring, False, align="Left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

###meow
meows = ["Meeowowwow", "mow", "meeep", "DREAMIES", "meeowwow"]
meow = turtle.Turtle()
meow.speed(0)
meow.color("white")
meow.penup()
meowstring = "Meeeeeow"
meow.hideturtle

#meow.setposition(-290, 280)
###create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("gun.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

###chose number of enemys
number_of_enemies = 5
enemies = []

#add enemies to list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
#    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(200, 250)
    enemy.setposition(x, y)

enemyspeed = 10




### Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"

###move player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280

    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    player.setx(x)
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bullet state as global if it needs changed
    global bulletstate
    if bulletstate =="ready":
        bulletstate ="fire"
            #move bullet to player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False

#def isMeow(bullet, enemies):
#    if isCollision == True:
#            ###random meow
#            meow.setposition(x, y)
#            meow.write(random.choice(meows), False, align="center", font=("Arial", 14, "normal"))
    



#keyboard
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

###main game loop
while True:

    for enemy in enemies:
        #move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        #move enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:

                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
            

        if enemy.xcor() < -280:
            for e in enemies:

                y = e.ycor()
                y -= 40                
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):

            #hide bullet
            bullet.hideturtle()
            bulletstate == "ready"
            bullet.setposition(0, -400)
            #reset enemy
            x = random.randint(-200, 200)
            y = random.randint(150, 250)
            enemy.setposition(x, y)
            #update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="Left", font=("Arial", 14, "normal"))
 #           isMeow

            ###game endding
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            ####game end
            end = turtle.Turtle
            end.shape("Untitled.gif")
            end.penup(0)
            end.setposition(0,0)
            end.speed(0)
            
            
            
            #break


    
        #move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

        ###bullet go past border reset
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"



#wn.mainloop()
delay = input("Press enter")


###vid 4 - 12:12