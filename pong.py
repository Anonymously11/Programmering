from cmu_graphics import *
class Ball(object):
    def __init__(self):
        self.body = Circle(200,200,20)
        self.xmove = 0
        self.ymove = 0
        self.pl1score = Label(0,250,100)
        self.pl2score = Label(0,150,100)

    def move(self):
        self.body.centerY += self.ymove
        self.body.centerX += self.xmove
        if (self.body.centerY > 380) or (self.body.centerY < 20):
            self.ymove = -self.ymove
        if ((self.body.centerX < 345) and (self.body.centerX > 55)):
            if self.body.hitsShape(player):
                self.ymove += (self.body.centerY-player.centerY)/10
                self.xmove = -self.xmove
            if self.body.hitsShape(player2):
                self.xmove = -self.xmove
        if self.body.centerX == 20:
            self.ymove = 0
            self.xmove = 0
            self.body.centerY = 200
            self.body.centerX = 200
            self.pl1score.value += 1
        if self.body.centerX == 380:
            self.ymove = 0
            self.xmove = 0
            self.body.centerY = 200
            self.body.centerX = 200
            self.pl2score.value += 1


player2 = Rect(355,150,15,70)
player = Rect(30,150,15,70)

ball1 = Ball()

app.uplist = ["w", "W"]
app.downlist = ["s","S"]
def onKeyHold(keys):
    for key in keys:
        if key in app.uplist:
            player.centerY -= 10
        if key in app.downlist:
            player.centerY += 10
    if "up" in keys:
        player2.centerY -= 10
    if "down" in keys:
        player2.centerY += 10

def onKeyPress(key):
    if key == "r":
        ball1.pl1score.value = 0
        ball1.pl2score.value = 0
    if ball1.xmove == 0:
        if key == "space":
            ball1.xmove = 5
            ball1.ymove = randrange(-3, 3)

def onStep():
    ball1.move()
    uncleverfying = randrange(-2,2)
    if uncleverfying < 1.7 and uncleverfying > -1.7:
        if ball1.body.centerY < player2.centerY:
            updown = -4
        else:
            updown = 4
    else:
        updown = 0
    player2.centerY += updown+uncleverfying

cmu_graphics.run()