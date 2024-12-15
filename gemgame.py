import pgzrun
import random
WIDTH=600
HEIGHT=600
TITLE='Gem flight'
gem=Actor('gemred')
gem.x=random.randint(70,WIDTH-70)
gem.y=10
schip=Actor('playership3_red')
schip.x=random.randint(70,WIDTH-70)
schip.y=550
gameover=False
score=0
def update():
    global gameover,score
    if keyboard.left:
        schip.x-=5
        if schip.x<0:
            schip.x=10
    if keyboard.right:
        schip.x+=5
        if schip.x>WIDTH:
            schip.x=10
    gem.y+=5
    if gem.y>HEIGHT:
        gameover=True
    if gem.colliderect(schip):
        score=score+1
        gem.x=random.randint(70,WIDTH-70)
        gem.y=10
    


def on_mouse_move(pos):
    schip.x=pos[0]


    
def draw():
    screen.clear()
    screen.fill('gray')
    if gameover:
        screen.draw.text('gameover',(250,250))
        screen.draw.text('score'+str(score),(250,300))
    else:
        screen.draw.text('score'+str(score),(250,300))

        schip.draw
    gem.draw()
    schip.draw()
    

    





















pgzrun.go()