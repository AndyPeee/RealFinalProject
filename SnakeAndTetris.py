import pygame
import random
import time
def score_test(snek, noms, randx, randy):
    if pygame.sprite.collide_rect(left=randx, right=randy):
        return 1
    else:
        return 10000000000
def food(window):
    picture = pygame.image.load("download.png")
    picture = pygame.transform.scale(picture, (50, 50))
    randy = random.randint(0, 1000)
    randx = random.randint(0, 1000)
    window.blit(picture, [randy, randx])
def snake():
    score = 0
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("SNAKE")
    x = 50
    y = 50
    w = 50
    h = 50
    velocity = 20
    run = True
    up = False
    down = False
    left = True
    right = False
    first_time = True
    while run:
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
        window.fill((0, 0, 0))
        snek = pygame.draw.rect(window, (255, 0, 0), (x, y, w, h))
        pygame.draw.rect(window, (255, 0, 0), (x, y, w, h))
        noms = pygame.image.load("download.png")
        noms = pygame.transform.scale(noms, (50, 50))
        if score == 0 and first_time:
            food(window)
            first_time = False
        if score_test(snek, noms) == 1:
            food(window)
            score += score
        pygame.display.update()
    pygame.quit()


snake()
