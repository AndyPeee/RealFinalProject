""" These next few lines imports the required systems/functions that need to be used in the process """
import pygame
import sys
import random
""" These lines establish variables that will be used later in the program """
randy = 0
randx = 0
tail = []

#Mr Stubbs added this

""" Shout out to Mr. Stubbs for all this, you the real MVP """
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


""" The score_test function constantly runs, and if the sprites are touching (the noms is touching the snek) 
it returns 1, which increases the score. This is constantly happening as it is in a while-loop, so it returns either
1's or 0's, which in turn functions like a short-term boolean """


def score_test(snek, noms, randx, randy):
    if noms.rect.colliderect(snek.rect): # this line checks to see if the rectangle shaped noms is being touched by snek
        return 1
    else:
        return 0


""" The food variable sets up the random coordinates that are constantly being used and changed each time the
food is touched """


def food():
    global randx, randy
    randy = random.randint(0, 400) # makes a random number within the boundary of the screen. This number will be used as a x or y coordinate for the food
    randx = random.randint(0, 400)


""" This next function is the main part of game. It initiates the game and calls on the other functions for variables
but otherwise contains the foundation of the game """

def snake():
    score = 0 # resets the score at the beginning of the game before the game starts to be changed later and acurately display the users score
    pygame.init() # starts the pygame system to be used later
    window = pygame.display.set_mode((500, 500)) # sets the display size for the window to be opened
    pygame.display.set_caption("SNAKE") # sets the name displayed at the top of the window to be opened
    x = 300 # sets up the starting position of the snake
    y = 300
    snek = Blocks("images.png", 50, 50) # takes the image used and creates a sprite with the image and scales it to a square
    window.fill((0, 0, 0)) # fills the screen with the color black as that is the background that will be used in the rest of the game
    noms = Blocks("download.png", 50, 50) # same as line 66
    velocity = 20 # sets the speed that the snake will move at by either adding or subtracting to the x or y
    run = True # if run is true the while-loop that contains the game basis starts
    up = True # establishes the bools to be used for movement, up is True because that is the direction in which the snake starts moving
    down = False # same as line 71
    left = False # same as line 71
    right = False # same as line 71
    first_time = True # if true it runs the food function for the first time
    while run: # this while loop is constantly making the game update to the positions and also allows for constant interaction for the user
        snek.update_pos(x, y) # at the beginning, the snake needs to be changed to its new position based off the users actions
        noms.update_pos(randx, randy) # if the food was collected this will update the food to it's new location
        window.fill((0, 0, 0)) # this fills the background of the image so that only the most recent position of the sprites is visible
        window.blit(snek.image, (x, y)) # this assures that the snake will be visible over the background
        firstup = True # this bool starts as true, and will be changed to false right after the first food is picked up. It will be used to prove that it is the first time picking up food and that the program should run one part rather than another
        for i in range(0, len(tail)): # this for loop constantly updates the food trailing the snake/body of the snake so that all the parts are following each other
            t = tail[i] # constantly changing "t" to equal the position in which it was picked up (first, second, etc.)
            if firstup: # for the first time the block only needs to follow 50 pixels behind in the given direction
                firstup = False # once the first time has occured, the bool changes to False so it doesn't happen again
                if up: # the direction that the food follows behind the snake is dependent on which direction the snake is moving, and the bools up, down, left, and righ indicate which direction has been selected by the user for the snake to travel in
                    t.update_pos(x, y+50)
                if down:
                    t.update_pos(x, y-50)
                if left:
                    t.update_pos(x+50, y)
                if right:
                    t.update_pos(x-50, y)
            else:
                if up: # if it is not the first time for the snake to eat food it takes the value of "t" (the order picked up) and places it in its respective section behind the snake and all other food picked up before it.
                    t.update_pos(tail[i-1].rect.x, tail[i-1].rect.y+50)
                if down:
                    t.update_pos(tail[i-1].rect.x, tail[i-1].rect.y-50)
                if left:
                    t.update_pos(tail[i-1].rect.x+50, tail[i-1].rect.y)
                if right:
                    t.update_pos(tail[i-1].rect.x-50, tail[i-1].rect.y)
            window.blit(t.image, (t.rect.x, t.rect.y)) # this shows the food behind the snake no-matter if it's the first time or not
        window.blit(noms.image, (randx, randy)) # this creates a new food to be picked up after the previous one was
        pygame.time.delay(100)
        if x < 0 or x > 500 or y < 0 or y > 500: # this if-statement checks to see if the user is outside of the boundary of the screen, and therefor loses
            print("Your score is: " + str(score)) # shows the final score at the end
            pygame.quit() # ends the game after the player goes out of bounds
            sys.exit(0)
        if score == 0 and first_time: # creates the food for the first time. Later in the game the food will be created as the previous one is consumed
            food()
            first_time = False
        if score_test(snek, noms, randx, randy) == 1: # checks if the sprites ever touch, a 0 means it hasn't and the statement doesn't occur, but a 1 means it did and it creates a new food, increases the score, and adds a block to the list of sprites following the snake around
            food()
            tail.append(Blocks("download.png", 50, 50))
            score += 1
        for event in pygame.event.get(): # if the user wants to end the game they can by clicking on the "X" at the top of the window
            if event.type == pygame.QUIT:
                print("Your score is:" + str(score)) #displays the score if you end the game early
                pygame.quit()
                sys.exit(0)
        keys = pygame.key.get_pressed() # takes in the user input of which key is pressed
        if keys[pygame.K_LEFT]: # depending on which key is pressed, that direction will become True and the rest False to tell the snake which direction it should move in
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
        if up: # depending on which key is pressed, one of the 4 directional bools will be True, and the velocity is either added to or subtracted from the x or y coordinate of the snake and creates a new position for it, making it seem as if the snake is gliding across the screen
            y -= velocity
        if down:
            y += velocity
        if left:
            x -= velocity
        if right:
            x += velocity
        pygame.display.update() # updates the window to the newest position of the snake after the movement has occured
    print("Your score is: " + str(score)) # displays the score if for some reason the game ends without any of the other score displaying segments getting triggered


snake() # starts the game
