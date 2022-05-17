from cmu_graphics import *
class Ball(object):
    def __init__(self):
        self.body = Circle(200,200,20)
        self.xmove = 0
        self.ymove = 0
        Label("scores", 200,50)
        Label(":", 200, 100)
        self.pl1score = Label(0,225,100)
        self.pl2score = Label(0,175,100)

    def move(self):
        self.body.centerY += self.ymove
        self.body.centerX += self.xmove
        if (self.body.centerY > 380) or (self.body.centerY < 20):
            self.ymove = -self.ymove

        # to prevent the ball to bounce/get stuck inside the player
        # (not the best solution)    
        if ((self.body.centerX < 340) and (self.body.centerX > 60)):
            for player in app.players:
                if self.body.hitsShape(player):
                    # don't know what is better just "=" or "+="
                    self.ymove += (self.body.centerY-player.centerY)/10
                    self.xmove = -self.xmove

        # can't write "or" because self.pl1score.value += 1
        if self.body.centerX == 20:
            app.instructions.visible = True
            self.ymove = 0
            self.xmove = 0
            self.body.centerY = 200
            self.body.centerX = 200
            self.pl1score.value += 1

        if  self.body.centerX == 380:
            app.instructions.visible = True
            self.ymove = 0
            self.xmove = 0
            self.body.centerY = 200
            self.body.centerX = 200
            self.pl2score.value += 1


player2 = Rect(355,150,15,70)
player = Rect(30,150,15,70)

ball1 = Ball()
app.players = [player, player2]
app.uplist = ["w", "W"]
app.downlist = ["s","S"]
def onKeyHold(keys):
    for key in keys:
        if key in app.uplist:
            player.centerY -= 10
        if key in app.downlist:
            player.centerY += 10
        if key == "up":
            player2.centerY -= 10
        if key == "down":
            player2.centerY += 10

app.instructions = Group(
    Label("space to start", 200, 250),
    Label("W and S keys", 50, 240),
    Label("up and down keys", 340, 240)
)
def onKeyPress(key):
    if key == "r":
        ball1.pl1score.value = 0
        ball1.pl2score.value = 0
    if ball1.xmove == 0:
        if key == "space":
            app.instructions.visible = False
            ball1.ymove = randrange(-3, 3)
            if randrange(0,10) > 4:
                ball1.xmove = 5
            else:
                ball1.xmove = -5

def onStep():
    ball1.move()

    #uncomment if you want to play alone
    # uncleverfying = randrange(-2,2)
    # if uncleverfying < 1.7 and uncleverfying > -1.7:
    #     if ball1.body.centerY < player2.centerY+uncleverfying:
    #         updown = -4
    #     else:
    #         updown = 4
    # else:
    #     updown = 0
    # player2.centerY += updown

cmu_graphics.run()