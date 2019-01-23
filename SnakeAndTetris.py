import pygame, sys
import random

randy = 0
randx = 0
tail = []

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

    def update_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y


def score_test(snek, noms, randx, randy):

   # if pygame.sprite.collide_rect(snek, noms):
    if noms.rect.colliderect(snek.rect):

        return 1
    else:
        return 0
def food(window, noms):
    global randx, randy
    #noms = pygame.image.load("download.png")
    #noms = pygame.transform.scale(noms, (50, 50))
    randy = random.randint(0, 400)
    randx = random.randint(0, 400)

def snake():
    score = 0
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SNAKE")
    x = 300
    y = 300
    w = 50
    h = 50
    snek = Blocks("images.png", 50, 50)
    pygame.draw.rect(window, (255, 0, 0), (x, y, w, h))
    window.fill((0, 0, 0))
    noms = Blocks("download.png", 50, 50)
    velocity = 20
    run = True
    up = True
    down = False
    left = False
    right = False
    first_time = True
    while run:
        snek.update_pos(x, y)
        noms.update_pos(randx, randy)
        window.fill((0, 0, 0))
        window.blit(snek.image, (x, y))
        firstup = True
        for i in range(0, len(tail)):
            t = tail[i]
            if firstup:
                firstup = False
                if up:
                    t.update_pos(x,y+50)
                if down:
                    t.update_pos(x,y-50)
                if left:
                    t.update_pos(x+50,y)
                if right:
                    t.update_pos(x-50,y)
            else:
                if up:
                    t.update_pos(tail[i-1].rect.x, tail[i-1].rect.y+50)
                if down:
                    t.update_pos(tail[i-1].rect.x, tail[i-1].rect.y-50)
                if left:
                    t.update_pos(tail[i-1].rect.x+50, tail[i-1].rect.y)
                if right:
                    t.update_pos(tail[i-1].rect.x-50, tail[i-1].rect.y)
            window.blit(t.image, (t.rect.x, t.rect.y))
        window.blit(noms.image, (randx, randy))
        pygame.time.delay(100)

        if x < 0 or x > 500 or y < 0 or y > 500:
            print("Your score is: "+str(score))
            pygame.quit()
            sys.exit(0)
        if score == 0 and first_time:
            food(window, noms)
            first_time = False
        if score_test(snek, noms, randx, randy) == 1:
            food(window, noms)
            tail.append(Blocks("download.png", 50, 50))
            score += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Your score is:" + str(score))
                pygame.quit()
                sys.exit(0)

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
        #window.blit(noms.image, (x,y))

        pygame.display.update()
    print("Your score is: " + str(score))


snake()
