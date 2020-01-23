#Name:Alex Pierce 
#bumper.py

#Purpose:Create program that creates two circles of different color
#and chooses inital random directions for them to move.

#Inputs:No user inputs

#Outputs:Two circles of different colors bouncing around window changing
#color and direction after collision with one another or wall.


from graphics import *
from time import sleep
import random
import math

#returns a random number between –moveAmount and + moveAmount
def getRandom(moveAmount):
    return random.randint(moveAmount*-1,moveAmount)

#returns Boolean based on the collision of the two balls
def didCollide(ball1,ball2):
    ball1X= ball1.getCenter().getX()
    ball1Y= ball1.getCenter().getY()
    ball1R=ball1.getRadius()
    ball2X=ball2.getCenter().getX()
    ball2Y=ball2.getCenter().getY()
    ball2R=ball2.getRadius()
    distance = (math.sqrt(((ball2X-ball1X)**2) + ((ball2Y-ball1Y)**2)))
    radius = ball1R + ball2R 
    if distance <= radius:
        return True
    else:
        return False

#returns True if ball hits a vertical wall, False otherwise
def hitVertical(ball, win):
    ballX= ball.getCenter().getX()
    ballRadius=ball.getRadius()
    if ballX >= 500-ballRadius or ballX <= ballRadius:
        return True
    else:
        return False
    
#returns True if ball hits a horizontal wall, False otherwise
def hitHorizontal(ball, win):
    ballY=ball.getCenter().getY()
    ballRadius = ball.getRadius()
    if ballY >= 500-ballRadius or ballY <= ballRadius:
        return True
    else:
        return False
    
#returns a random color 
def randomColor(ball):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    ball.setFill(color_rgb(r, g, b))

def main():
    #create window
    win=GraphWin("Bumper Car Simulation", 500, 500)
    #create and draw ball1
    ball1=Circle(Point(100,100),30)
    ball1.setFill("Red")
    ball1.draw(win)
    #create and draw ball2
    ball2=Circle(Point(100,300),30)
    ball2.setFill("Blue")
    ball2.draw(win)
    #set initial velocities of balls through getRandom function
    ball1XSpeed= getRandom(15)
    ball1YSpeed= getRandom(15)
    ball2XSpeed= getRandom(15)
    ball2YSpeed= getRandom(15)
    #set speed [x,y]
    speed= [[ball1XSpeed,ball1YSpeed],[ball2XSpeed,ball2YSpeed]]
    #loop to make balls move
    for i in range (1000):
        sleep(.05)
        ball1Move= ball1.move(speed[0][0],speed[0][1])
        ball2Move= ball2.move(speed[1][0],speed[1][1])
        if hitVertical(ball1, win):
           speed[0][0] = (-speed[0][0])
           randomColor(ball1)
        if hitHorizontal(ball1, win):
            speed[0][1] = (-speed[0][1])
            randomColor(ball1)
        if hitVertical(ball2, win):
            speed[1][0] = (-speed[1][0])
            randomColor(ball2)
        if hitHorizontal(ball2,win):
            speed[1][1] = (-speed[1][1])
            randomColor(ball2)
        if didCollide(ball1,ball2):
            speed[0][0] = (-speed[0][0])
            speed[0][1] = (-speed[0][1])
            speed[1][0] = (-speed[1][0])
            speed[1][1] = (-speed[1][1])
            randomColor(ball1)
            randomColor(ball2)
            




main()

                      
