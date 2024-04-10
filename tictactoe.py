import pygame

win = pygame.display.set_mode((450, 450))


class Board:

    def draw_line(self):
        pygame.draw.line(win,(255,0,0),(150,0),(150,450),6)
        pygame.draw.line(win,(255, 0, 0), (300,0), (300, 450),6  )
        pygame.draw.line(win,(255, 0, 0), (0, 150), (450, 150),6 )
        pygame.draw.line(win,(255, 0, 0), (0,300), (450, 300),6 )

    def drawkrest(self):
        pos = pygame.mouse.get_pos()

        pygame.draw.line(win, (0, 255, 0), ((pos[0] - 50), (pos[1] - 50)), ((pos[0] + 50), (pos[1] + 50)), 5)
        pygame.draw.line(win, (0,255 , 0), ((pos[0] - 50), (pos[1] + 50)), ((pos[0] + 50), (pos[1] - 50)), 5)

    def drawCircle(self):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(win,(0, 255, 0), pos ,50)


board = Board()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 0))
    board.draw_line()
    board.drawkrest()
    board.drawCircle()
    pygame.display.update()
    pygame.time.delay(20)
