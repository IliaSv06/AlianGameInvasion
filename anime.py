from pygame.sprite import Sprite
import pygame

class Explosion(Sprite):
    def __init__(self, center):
        super(Explosion, self).__init__()
        self.images_boom = []
        for number in range(9):
            image_boom = pygame.image.load(f'animation/regularExplosion0{number}.png')
            image_boom = pygame.transform.scale(image_boom, (100, 100))
            self.images_boom.append(image_boom)

        self.index = 0
        self.image = self.images_boom[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.conteiner = 0

    def update(self):
        self.speed_image = 4
        self.conteiner+=1
        if self.conteiner >= self.speed_image and self.index < len(self.images_boom) - 1:
            self.conteiner = 0
            self.index+=1
            self.image = self.images_boom[self.index]

        if self.conteiner >= self.speed_image and self.index >= len(self.images_boom) - 1:
            self.kill()

