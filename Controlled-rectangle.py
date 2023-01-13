import pygame

# Initialize pygame
pygame.init()

# Set the size of the window
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Controlled Rectangle")

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set the player's initial position
player_x = 350
player_y = 250

# Initialize the player's speed
player_speed = 5

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Clear the screen
    screen.fill(white)

    # Draw the player
    pygame.draw.rect(screen, black, (player_x, player_y, 50, 50))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
