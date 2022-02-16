import pygame
from pygame.sprite import Sprite

class Alien (Sprite):
    '''a class to represent a single alien in the fleet'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien's ship
        self.image = pygame.image.load('images/circular_ship.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # store the alien's exact horizental position
        self.x = self.rect.x
        

    def update(self):
        '''move the alien to the right'''
        self.x += (self.settings.alien_speed) * (self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
