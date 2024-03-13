import pygame
pygame.init()
pygame.display.set_mode()

class Circle:
    def __init__(self,radius,x, y, surface, color):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.radius =  radius

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x,self.y), self.radius)

   def move_by_keys(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
           self.x -= 3
       elif keys[pygame.K_RIGHT]:
           self.x += 3
       elif keys[pygame.K_UP]:
           self.y -= 3
       elif keys[pygame.K_DOWN]:
           self.y += 3


##создать объект

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    win.fill((0, 225, 225))
    #вызываем методы


    pygame.time.delay(10)
    pygame.display.update()