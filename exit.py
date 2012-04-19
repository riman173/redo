from levelformat import Exit as e
import os
import pygame

class Exit(pygame.sprite.Sprite):
    image = None
    def __init__(self, exitFormat):
        if not Exit.image:
            imgpath = os.path.join("assets", "images", "exit.png")
            Exit.image = pygame.image.load(imgpath).convert_alpha()
        self.image = Exit.image
        self.rect = self.image.get_rect()
        self.rect.center = exitFormat.rect.center
