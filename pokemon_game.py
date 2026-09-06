import pgzrun
import random
from pgzClasses import *

#===================
#    GAME INFO
#===================

WIDTH = 640
HEIGHT = 480
TITLE = "Pokemon Red - Citrus Attack!"


#===================
#      ACTORS
#===================

player = Actor("player")
player.speed = 4
enemies = []
projectiles = []
bg = Actor("level1")
bg2 = Actor("level2")
bg3 = Actor("level3")

#===================
#     VARIABLES
#===================

score = 0
spawn_rate = 60.0  # Starting spawn chance (1 in 60 frames)
game_scene = "title"

#==================
#      SETUP
#==================

def game_setup():
    global enemies, projectiles, score, spawn_rate
    enemies.clear()
    projectiles.clear()
    score = 0
    spawn_rate = 60.0  # Reset the difficulty when retrying

    # Place player at the bottom center of the screen
    player.x = WIDTH // 2
    player.y = HEIGHT - 40

#===================
#     CONTROLS
#===================

def player_movement():
    # Horizontal movement only, bounded to the window edges
    if (keyboard.right or keyboard.d) and player.x < WIDTH - player.width // 2:
        player.x += player.speed
    elif (keyboard.left or keyboard.a) and player.x > player.width // 2:
        player.x -= player.speed


def projectile_movement():
    global score, game_scene

    for projectile in projectiles.copy():
        projectile.y += projectile.vy

        hit_enemy = False
        for enemy in enemies.copy():
            if projectile.colliderect(enemy):
                enemies.remove(enemy)
                score += 1
                hit_enemy = True
                break

        if hit_enemy:
            projectiles.remove(projectile)
            continue

        # Despawn projectile if it goes off the top of the screen
        if projectile.y < 0:
            projectiles.remove(projectile)

        # FIX 1: Only trigger the transition if we are currently in "level" 1
    if game_scene == "level":
        if score == 30:
            enemies.clear()  # Clear old enemies so they don't instantly kill you in level 2
            projectiles.clear()  # Clear old bullets
            game_scene = "passing"

    # FIX: Isolate level 2 passing2 check so it doesn't conflict with Level 1
    elif game_scene == "level2":
        if score >= 50:  # Change 5 to whatever target score you want for Level 2!
            game_scene = "passing2"


# FIX: Isolate level 3 victory check so it doesn't conflict with Level 2 or Level 1
    elif game_scene == "level3":
        if score >= 75:  # Change 5 to whatever target score you want for Level 3!
            game_scene = "victory"

def enemy_movement():
    global game_scene, spawn_rate, enemies
    # Gradually decrease the spawn limit to make enemies appear more frequently
    if spawn_rate > 10.0:
        spawn_rate -= 0.02
    if game_scene == "level":
        # Randomly spawn an enemy based on the current spawn_rate limit
        if random.randint(1, int(spawn_rate)) == 1:
            enemy = Actor("enemy", (random.randint(32, WIDTH - 32), -40))
            # Give the enemy a random falling speed
            enemy.vy = random.uniform(2.0, 4.0)
            enemies.append(enemy)

        for enemy in enemies.copy():
            enemy.y += enemy.vy

            # End game if an enemy touches the player
            if enemy.colliderect(player):
                game_scene = "game_over"

            # Despawn enemy if it passes the bottom of the window
            if enemy.y > HEIGHT + 40:
                enemies.remove(enemy)
    #---------------------- ENEMY2 -------------------
    elif game_scene == "level2":
        if random.randint(1, int(spawn_rate)) == 1:
            enemy2 = Actor("enemy2", (random.randint(32, WIDTH - 32), -40))
            # Give the enemy a random falling speed
            enemy2.vy = random.uniform(2.0, 4.0)
            enemies.append(enemy2)

        for enemy2 in enemies.copy():
            enemy2.y += enemy2.vy

            # End game if an enemy touches the player
            if enemy2.colliderect(player):
                game_scene = "game_over"

            # Despawn enemy if it passes the bottom of the window
            if enemy2.y > HEIGHT + 40:
                enemies.remove(enemy2)

    elif game_scene == "level3":
        if random.randint(1, int(spawn_rate)) == 1:
            enemy3 = Actor("enemy3", (random.randint(32, WIDTH - 32), -40))
            # Give the enemy a random falling speed
            enemy3.vy = random.uniform(2.0, 4.0)
            enemies.append(enemy3)

        for enemy3 in enemies.copy():
            enemy3.y += enemy3.vy

            # End game if an enemy touches the player
            if enemy3.colliderect(player):
                game_scene = "game_over"

            # Despawn enemy if it passes the bottom of the window
            if enemy3.y > HEIGHT + 40:
                enemies.remove(enemy3)


def on_key_down(key):
    global game_scene

    if game_scene == "level":
        # Press Space or J to shoot upward
        if key == keys.SPACE or key == keys.J:
            projectile = Actor("projectile", (player.x, player.y))
            projectile.vy = -8
            projectiles.append(projectile)


    elif game_scene == "level2":
        # Press Space or J to shoot upward
        if key == keys.SPACE or key == keys.J:
            projectile = Actor("projectile", (player.x, player.y))
            projectile.vy = -8
            projectiles.append(projectile)

    elif game_scene == "level3":
        # Press Space or J to shoot upward
        if key == keys.SPACE or key == keys.J:
            projectile = Actor("projectile", (player.x, player.y))
            projectile.vy = -8
            projectiles.append(projectile)


    elif game_scene == "title":
        if key == keys.SPACE:
            game_scene = "level"
    elif game_scene == "game_over" or game_scene == "victory":
        if key == keys.R:
            game_scene = "title"
    elif game_scene == "passing":
        if key == keys.N:
            # score = 0
            game_scene = "level2"
    elif game_scene == "passing2":
        if key == keys.Y:
            game_scene = "level3"
    elif game_scene == "passing3":
        if key == keys.E:
            game_scene = "evolution!"
    elif game_scene == "evolution!":
        if key == keys.T:
            game_scene = "level4"

#===================
#  UPDATE AND DRAW
#===================

def update():
    if game_scene == "level" or game_scene == "level2" or game_scene == "level3":
        player_movement()
        projectile_movement()
        enemy_movement()


def draw():
    global game_scene

    #-------------------
    #       LEVEL
    #-------------------
    if game_scene == "level":
        #screen.fill("lightgoldenrod1")
        bg.draw()
        for enemy in enemies:
            enemy.draw()
        for projectile in projectiles:
            projectile.draw()
        player.draw()

        # Draw the score bar
        screen.draw.filled_rect(Rect(0, 0, WIDTH, 40), "black")
        screen.draw.text("Score: " + str(score), (10, 10), color="white", fontsize=30)

    #-------------------
    #       LEVEL
    #-------------------
    elif game_scene == "level2":
        #screen.fill("lightgoldenrod1")
        bg2.draw()
        for enemy2 in enemies:
            enemy2.draw()
        for projectile in projectiles:
            projectile.draw()
        player.draw()

        # Draw the score bar
        screen.draw.filled_rect(Rect(0, 0, WIDTH, 40), "black")
        screen.draw.text("Score: " + str(score), (10, 10), color="white", fontsize=30)

    elif game_scene == "level3":
        #screen.fill("lightgoldenrod1")
        bg3.draw()
        for enemy3 in enemies:
            enemy3.draw()
        for projectile in projectiles:
            projectile.draw()
        player.draw()

        # Draw the score bar
        screen.draw.filled_rect(Rect(0, 0, WIDTH, 40), "black")
        screen.draw.text("Score: " + str(score), (10, 10), color="white", fontsize=30)



    #-------------------
    #       TITLE
    #-------------------
    elif game_scene == "title":
        game_setup()
        screen.fill("lightsalmon")
        screen.draw.text(TITLE, (65, 180), color="white", fontsize=50)
        screen.draw.text("Press SPACE to Start", (200, 260), color="white", fontsize=25)

    #-------------------
    #     GAME OVER
    #-------------------
    elif game_scene == "game_over":
        screen.fill("darkred")
        screen.draw.text("GAME OVER", (200, 180), color="white", fontsize=50)
        screen.draw.text("Press R to Try Again", (210, 260), color="white", fontsize=25)

    #-------------------
    #     LEVEL 2
    #-------------------
    elif game_scene == "passing":
        screen.fill("lightgoldenrod1")
        screen.draw.text("Congrats! You've passed to next level!", (5, 180), color="white", fontsize=50)
        screen.draw.text("Press N to Continue", (210, 260), color="white", fontsize=25)

    elif game_scene == "passing2":
        screen.fill("lightskyblue")
        screen.draw.text("Congrats! You've passed to next level!", (5, 180), color="white", fontsize=50)
        screen.draw.text("Press Y to Continue", (210, 260), color="white", fontsize=25)

    elif game_scene == "victory":
         screen.fill("lightgreen")
         screen.draw.text("You have beaten the Citrusdrops!",  (40, 180), color="white", fontsize=50)
         screen.draw.text("You and your friends are safe now!",  (35, 230), color="white", fontsize=50)
         screen.draw.text("Press R to Go Again", (210, 300), color="white", fontsize=25)

pgzrun.go()

