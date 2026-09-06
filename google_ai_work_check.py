def enemy_movement():
    global game_scene, spawn_rate, enemies

    # Gradually decrease the spawn limit to make enemies appear more frequently
    if spawn_rate > 10.0:
        spawn_rate -= 0.02

    # Randomly spawn an enemy based on the current spawn_rate limit
    if random.randint(1, int(spawn_rate)) == 1:
        # --- NEW SPRITE SELECTION LOGIC ---
        if game_scene == "level2":
            enemy_image = "enemy2"  # Put the name of your Level 2 sprite file here
        else:
            enemy_image = "enemy"  # Your original Level 1 sprite

        enemy = Actor(enemy_image, (random.randint(32, WIDTH - 32), -40))
        # ----------------------------------

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


# To change the enemy sprite in Level 2, you just need to pass a different image name to the Actor() constructor when spawning them inside your enemy_movement() function.
# Right now, your code always spawns "enemy". By adding a quick if/else check, you can tell it to use your new sprite whenever game_scene == "level2".
# Step 1: Update your enemy_movement functionReplace your current enemy_movement() function with this code.
# Make sure you have a second image file saved in your images folder (for example, named "enemy2"):