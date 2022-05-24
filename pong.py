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
        self.timer = 0

    def move(self):
        self.body.centerY += self.ymove
        self.body.centerX += self.xmove
        pastY = self.body.centerY
        if (self.body.centerY > 380) or (self.body.centerY < 20):
            self.body.centerY = pastY
            self.ymove = -self.ymove

        # to prevent the ball to bounce/get stuck inside the player
        # still it feels strange playing
        if self.timer < 1:
            for player in app.players:
                if self.body.hitsShape(player):
                    self.timer = 40
                    # don't know what is better just "=" or "+="
                    self.ymove += (self.body.centerY-player.centerY)/10
                    self.xmove = -self.xmove
        else:
            self.timer -= 1
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
app.amountplayers = 2
def automove():
    if app.amountplayers == 1:
        # to improve: make it more human
        uncleverfying = randrange(0,100)
        if uncleverfying > 70:
            if ball1.body.centerY < player2.centerY:
                app.updown = -8
            else:
                app.updown = 8
        else:
            app.updown = 0
        player2.centerY += app.updown

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
        if app.amountplayers != 1:
            if key == "up":
                player2.centerY -= 10
            if key == "down":
                player2.centerY += 10
Label("player(s)",200, 10)
app.numplayers = Label(app.amountplayers,200, 25)
app.instructions = Group(
    Label("space to start", 200, 250),
    Label("W and S keys", 50, 240),
    Label("up and down keys", 340, 240)
)
def onKeyPress(key):
    if key == "1":
        app.amountplayers = 1
        app.numplayers.value = app.amountplayers
    if key == "2":
        app.amountplayers = 2
        app.numplayers.value = app.amountplayers
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


app.updown = 0
def onStep():
    ball1.move()

    # uncomment if you want to play alone
    # or just press 1 for one player
    automove()

cmu_graphics.run()