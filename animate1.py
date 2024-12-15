import pgzrun

WIDTH=500
HEIGHT=300

object=Actor('apple')

object.pos=50,HEIGHT//2

def start_animation():
    animate(object,pos=(50,HEIGHT//2),duration=3)

def draw():
    screen.clear()
    object.draw()

def on_key_down():
    start_animation()

pgzrun.go()