import pygame
import sys
from character import Character

# Initialize pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Find The One Piece")

# Create character object
character = Character(SCREEN_WIDTH, SCREEN_HEIGHT)

# Main game loop
def main():
    clock = pygame.time.Clock()
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill((0, 0, 0))

        # Update character position
        character.update(keys)

        # Draw the character
        character.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

# Run the game
if __name__ == "__main__":
    main()
