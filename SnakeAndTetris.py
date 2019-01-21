import pygame
import random
import time

randy = 0
randx = 0

#Mr Stubbs added this
class Blocks(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, image, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

def score_test(snek, noms, randx, randy):
    if pygame.sprite.collide_rect(snek, noms):
        return 1

    else:
        return 0
def food(window):
    global randx, randy
    noms = pygame.image.load("download.png")
    noms = pygame.transform.scale(noms, (50, 50))
    randy = random.randint(0, 50)
    randx = random.randint(0, 50)
    window.blit(noms, [randy, randx])
def snake():
    score = 0
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("SNAKE")
    x = 50
    y = 50
    w = 50
    h = 50
    snek = Blocks("images.png", 50, 50)
    pygame.draw.rect(window, (255, 0, 0), (x, y, w, h))
    window.fill((0, 0, 0))
    noms = Blocks("download.png", 50, 50)
    velocity = 20
    run = True
    up = False
    down = True
    left = False
    right = False
    first_time = True
    #blit snek and noms
    while run:
        if score == 0 and first_time:
            food(window)
            first_time = False
        if score_test(snek, noms, randx, randy) == 1:
            print("test")
            food(window)
            print("test2")
            noms.kill()
            window.fill((0, 0, 0))
            score += 1

        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
            right = False
            down = False
            up = False
        if keys[pygame.K_RIGHT]:
            left = False
            right = True
            down = False
            up = False
        if keys[pygame.K_UP]:
            left = False
            right = False
            down = False
            up = True
        if keys[pygame.K_DOWN]:
            left = False
            right = False
            down = True
            up = False
        if up:
            y -= velocity
        if down:
            y += velocity
        if left:
            x -= velocity
        if right:
            x += velocity
        snek = Blocks("images.png", 50, 50)
        snek = pygame.image.load("images.png")
        snek = pygame.transform.scale(snek, (50, 50))
        window.blit(snek, [100, 100])
        pygame.display.update()
    pygame.quit()


snake()
