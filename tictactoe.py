import pygame

win = pygame.display.set_mode((500, 500))


class Board:
    def __init__(self, height, width,colo):
        self.height = height
        self.width = width
    def draw_line(self):
        pygame.draw.line(win,(255,0,0),150,150)


color = (0,0,0)
x = 150
y = 150

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



    win.fill((255,255,255))

    pygame.display.update()
