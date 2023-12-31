import pygame, sys
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x,self.y)
         # create an x and y position
         # draw a square

# create a rectangle
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x,self.pos.y,cell_size,cell_size)
        
        # draw the rectangle
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
       

        


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)

    # fills our test surface with the color blue = (test_surface.fill(pygame.Color(0,213,255))