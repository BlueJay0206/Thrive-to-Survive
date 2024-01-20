import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menu and Game Example")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up buttons
play_button = pygame.Rect(300, 200, 200, 50)
quit_button = pygame.Rect(300, 300, 200, 50)

# Function to show the menu
def show_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the mouse click is on a button
                if play_button.collidepoint(event.pos):
                    print("Play button clicked!")
                    # Add game start logic here
                    return "game"
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Fill the screen with a background color
        screen.fill(white)

        # Draw buttons
        pygame.draw.rect(screen, (0, 128, 0), play_button)
        pygame.draw.rect(screen, (128, 0, 0), quit_button)

        # Draw text on buttons
        play_text = font.render('Play', True, white)
        quit_text = font.render('Quit', True, white)
        screen.blit(play_text, (play_button.x + 70, play_button.y + 15))
        screen.blit(quit_text, (quit_button.x + 70, quit_button.y + 15))

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        pygame.time.Clock().tick(60)

# Function for the main game
def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Your main game logic goes here
        # ...

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        pygame.time.Clock().tick(60)

# Initial state is the menu
current_state = "menu"

# Main game loop
while True:
    if current_state == "menu":
        current_state = show_menu()
    elif current_state == "game":
        run_game()
