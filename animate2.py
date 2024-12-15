import pgzrun

# Screen dimensions
WIDTH = 500
HEIGHT = 300

# Define the Actor
character = Actor('run2')  # Replace 'character' with an actual image name like 'alien'
character.pos = 50, HEIGHT // 2  # Start position on the left

# Start animation to move the character across the screen
def start_animation():
    animate(character, pos=(WIDTH - 50, HEIGHT // 2), duration=2)

# Draw the character on the screen
def draw():
    screen.clear()
    character.draw()

# Start the animation when the game starts
start_animation()

# Run the Pygame Zero engine
pgzrun.go()
