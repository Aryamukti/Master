import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LAYAR_LEBAR,LAYAR_TINGGI))
        pygame.display.set_caption('Tanikita')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()
           
if __name__ == '__main__':
    game = Game()
    game.run()
     