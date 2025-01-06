import pygame,sys

pygame.init()
dark_blue = (44, 44, 127)

# configurações tela
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("TETRIS")

clock = pygame.time.Clock()

# loop para manter a tela aberta
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # desenho
    screen.fill(dark_blue)

    pygame.display.update()
    clock.tick(60) # 60 frames por segundo
