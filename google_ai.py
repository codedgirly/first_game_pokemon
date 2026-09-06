import pgzrun

# 1. Define game variables at the very top
current_level = 1
score = 0

# Set the game window size
WIDTH = 600
HEIGHT = 400


def draw():
    screen.clear()

    # 2. Draw different things depending on the level
    if current_level == 1:
        screen.fill("lightblue")
        screen.draw.text("LEVEL 1: Click the screen to score!", (50, 150), fontsize=30, color="black")
    elif current_level == 2:
        screen.fill("darkblue")
        screen.draw.text("LEVEL 2: Keep clicking!", (50, 150), fontsize=30, color="white")
    elif current_level == 3:
        screen.fill("purple")
        screen.draw.text("YOU WIN! Game Over.", (150, 150), fontsize=40, color="yellow")

    # Always show the score at the top left
    screen.draw.text(f"Score: {score}", (20, 20), fontsize=30, color="white")


def update():
    # 3. Tell Python we want to change 'current_level' inside this function
    global current_level

    # 4. Check score thresholds to change levels
    if score >= 5 and current_level == 1:
        current_level = 2
    elif score >= 12 and current_level == 2:
        current_level = 3


def on_mouse_down():
    # 5. Tell Python we want to change 'score' when clicked
    global score

    # Only add points if the game isn't finished yet
    if current_level < 3:
        score += 1


pgzrun.go()