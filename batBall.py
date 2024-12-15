import pgzrun

WIDTH = 500
HEIGHT = 500

ball = Rect((150, 400), (20, 20))
bat =  Rect((200, 480), (60, 20))
vx = 2
vy = 2
score=0
def draw():
    global score
    screen.clear()
    screen.draw.filled_rect(ball, "red")
    screen.draw.filled_rect(bat, "white")
    screen.draw.text("Score :"+str(score),(20,20),color="orange")

def update():
    global vx, vy,score
    ball.x += vx
    ball.y += vy
    if ball.right > WIDTH or ball.left < 0:
        vx = -vx
    if ball.colliderect(bat) or ball.top < 0:
        vy = -vy
        score=score+1
    if ball.bottom > HEIGHT:
        exit()
    if(keyboard.right):
        bat.x += 2
    if(keyboard.left):
        bat.x -= 2

pgzrun.go()