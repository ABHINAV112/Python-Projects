from turtle import Turtle,Screen


GameScreen = Screen()
GameScreen.setworldcoordinates(-300, -300, 300, 300)
count  = 0
TerrainT = Turtle()
TerrainT.hideturtle()
TerrainT.penup()
Jumper = Turtle()
Jumper.seth(90)
Jumper.penup()


def JumperJump():
    global count 
    if count == 0:
        count = 1 
        for i in range(25):
            Jumper.fd(2)
        for i in range(25):
            Jumper.bk(2)
        count = 0

def Terrain():
    TerrainT.goto(-300,-10)
    TerrainT.pendown()
    TerrainT.seth(0)
    TerrainT.fd(600)
    TerrainT.penup()

class Obstacle:
    def __init__(self):
        self.Obstacle = Turtle()
        self.Obstacle.hideturtle()
        self.Obstacle.penup()
        self.Obstacle.goto(300,0)
        self.Obstacle.seth(180)
        self.Obstacle.showturtle()

    def Movement(self):
        self.Obstacle.forward(2)


Terrain()

GameScreen.onkeypress(JumperJump,'Up')

ObstacleT = Obstacle()

while True:
    for i in range(300):

        ObstacleT.Movement()
        GameScreen.listen()
GameScreen.mainloop()
