from turtle import *
from random import *
from math import  *

GameScreen = Screen()
GameScreen.setworldcoordinates(-120,-120,120,150)

#turtle to count the score
ScoreTurtle = Turtle()
ScoreTurtle.hideturtle()
ScoreTurtle.speed(0)
ScoreTurtle.penup()
ScoreTurtle.pencolor('Cyan')
ScoreTurtle.goto(-120,125)
ScoreTurtle.pendown()

#setting up the snake turtle
Snake = Turtle()
Snake.speed(1)
Snake.shape('square')
Snake.resizemode('user')
Snake.shapesize(1/2,1/2,1/2)
Snake.color('green')
Snake.penup()

#to draw a boundary
Snake.hideturtle()
Snake.goto(-110,-110)
Snake.pendown()
Snake.speed(0)
Snake.color('Red')
Snake.seth(0)
for i in range(4):
    Snake.fd(220)
    Snake.lt(90)
Snake.penup()
Snake.color('Green')
Snake.showturtle()
Snake.goto(0,0)
Snake.speed(1)


    

#setting up the food turtle
food = Turtle()


def distance( tuple1 , tuple2 ):
    x=tuple1[0] - tuple2[0]
    y=tuple1[1] - tuple2[1]
    dist = sqrt(x**2 + y**2)
    return dist


def FoodGenerator():
    xfood = randint(-100,100)
    yfood = randint(-100,100)
    
    global food
    
    food.shape('circle')
    food.resizemode('user')
    food.shapesize(1/2,1/2,1/2)
    food.speed(0)
    food.penup()
    food.hideturtle()
    food.goto(xfood,yfood)

    food.showturtle()

    return xfood,yfood


#functions to make the turtle change angle
def up():
    Snake.seth(90)

def down():
    Snake.seth(270)

def left():
    Snake.seth(180)

def right():
    Snake.seth(0)


#to make the snake move according to input from the arrows
GameScreen.onkey(up,'Up')
GameScreen.onkey(down,'Down')
GameScreen.onkey(left,'Left')
GameScreen.onkey(right,'Right')
GameScreen.onkey(up,'w')
GameScreen.onkey(down,'s')
GameScreen.onkey(left,'a')
GameScreen.onkey(right,'d')
GameScreen.listen()

FoodCoords = FoodGenerator()

Time = 0
Speed = 1
Score = 0
WriteFont = ('Arial',14,'bold')
ScoreTurtle.write('Score: '+str(Score),font=WriteFont)

#to make the snake move, main program
while True:
    Snake.fd(1)
    SnakeCoords = (Snake.xcor() , Snake.ycor())
    Time += 1
    
    if distance(SnakeCoords , FoodCoords) < 4:
        FoodCoords = FoodGenerator()
        ScoreTurtle.clear()
        Score +=1    
        ScoreTurtle.write('Score: '+str(Score),font=WriteFont)
        '''
        if Score%5 == 0:
            Speed+=1
            Snake.speed(Speed)
        '''

    #for the snake to teleport to the other side if it runs to the edge
    if Snake.ycor() < -110:
        Snake.hideturtle()
        Snake.speed(0)
        Snake.sety(110)
        Snake.speed(1)
        Snake.showturtle()

    if Snake.ycor() > 110:
        Snake.hideturtle()
        Snake.speed(0)
        Snake.sety(-110)
        Snake.speed(1)
        Snake.showturtle()

    if Snake.xcor() < -110:
        Snake.hideturtle()
        Snake.speed(0)
        Snake.setx(110)
        Snake.speed(1)
        Snake.showturtle()

    if Snake.xcor() > 110:
        Snake.hideturtle()
        Snake.speed(0)
        Snake.setx(-110)
        Snake.speed(1)
        Snake.showturtle()



GameScreen.mainloop()