import pygame
import os

class Character:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.character_folder = os.path.join("graphics", "character", "luffy")
        # Load and resize the left-facing character image
        self.image_left = pygame.image.load(os.path.join(self.character_folder, "luffyLeft.png"))
        self.image_left = pygame.transform.scale(self.image_left, (self.image_left.get_width() // 4, self.image_left.get_height() // 4))
        # Load and resize the right-facing character image
        self.image_right = pygame.image.load(os.path.join(self.character_folder, "luffyRight.png"))
        self.image_right = pygame.transform.scale(self.image_right, (self.image_right.get_width() // 4, self.image_right.get_height() // 4))
        self.image = self.image_left  # Start with left-facing image by default
        self.rect = self.image.get_rect()
        self.rect.center = (self.screen_width // 2, self.screen_height // 2)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.image = self.image_left
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.image = self.image_right
            self.rect.x += 5
        elif keys[pygame.K_UP]:
            self.rect.y -= 5
        elif keys[pygame.K_DOWN]:
            self.rect.y += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)
