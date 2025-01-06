import pygame
import sys
from grid import Grid

pygame.init()
dark_blue = (44, 44, 127)

# configurações tela
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("TETRIS")

clock = pygame.time.Clock()

# definindo uma grid para o jogo
game_grid = Grid()
game_grid.print_grid()


# loop para manter a tela aberta
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # desenho
    screen.fill(dark_blue)
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(60) # 60 frames por segundo
