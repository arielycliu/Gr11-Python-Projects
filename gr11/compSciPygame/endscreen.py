import pygame
import random
import math

pygame.init()

# Creating a window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jan and Ari Mack a Mole")

restart = True


class Circle(object):
    def __init__(self, color, center, radius):
        self.color = color
        self.center = center
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.center, self.radius)


def redraw_game_window():
    win.fill(000)
    for circle in goodCircles:
        circle.draw(win)
    for circle in badCircles:
        circle.draw(win)
    pygame.display.update()  # code for redrawing stuff


def create_good_circles():

    num_of_circles = 3
    size = 30
    for i in range(num_of_circles):
        coord = random.choice(pos)  # choose a random location
        pos.remove(coord)  # Remove that possible spot
        goodCircles.append(Circle((164, 213, 208), coord, size))
        # if round over then restart pos# code to create instances of the object


def create_bad_circles():
    num_of_circles = 3
    size = 30
    for i in range(num_of_circles):
        coord = random.choice(pos)  # choose a random location
        pos.remove(coord)  # Remove that possible spot
        badCircles.append(Circle((255, 25, 58), coord, size))
        # if round over then restart pos# code to create instances of the object


def endscreen():
    global restart, goodCircles, badCircles
    restart = True
    print("HMMMM")

    goodCircles = []
    badCircles = []

    win.fill(000)
    pygame.display.update()
    largeFont = pygame.font.SysFont("courier", 40)
    roundText = largeFont.render("Round Over: " + str(score), True, (255, 255, 255))
    smallFont = pygame.font.SysFont("courier", 20)
    nextRound = smallFont.render("Press space to enter next round", True, (255, 255, 255))


    end = True
    while end:

        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check quit game
                global running
                running = False
                return
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            end = False

        win.blit(roundText, (80, 250))
        win.blit(nextRound, (60, 325))
        pygame.display.update()





# all possible positions for the circles on a five by five grid
pos = [(50, 50), (150, 150), (250, 250), (350, 350), (450, 450), (50, 150), (50, 250), (50, 350), (50, 450), (150, 50), (150, 250), (150, 350), (150, 450), (250, 50), (250, 150), (250, 350), (250, 450), (350, 50), (350, 150), (350, 250), (350, 450), (450, 50), (450, 150), (450, 250), (450, 350)]
goodCircles = []
badCircles = []
score = 0

running = True
while running:
    pygame.time.delay(100)  # rate



    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check quit game
            running = False

        if event.type == pygame.MOUSEBUTTONUP:  # check for click
            pos = pygame.mouse.get_pos()  # get position of click
            for circle in goodCircles:
                xm, ym = pos
                xc, yc = circle.center
                distance = math.hypot(xm - xc, ym - yc)  # calculate distance
                if distance <= circle.radius:  # compare distance of click from center of circle to radius of circle
                    goodCircles.remove(circle)  # delete the circle
                    score += 5

    if goodCircles == [] and score > 0: # make so not starting
        endscreen()

    if restart == True:
        pos = [(50, 50), (150, 150), (250, 250), (350, 350), (450, 450), (50, 150), (50, 250), (50, 350), (50, 450), (150, 50), (150, 250), (150, 350), (150, 450), (250, 50), (250, 150), (250, 350), (250, 450), (350, 50), (350, 150), (350, 250), (350, 450), (450, 50), (450, 150), (450, 250), (450, 350)]
        goodCircles = []
        badCircles = []
        create_good_circles()
        create_bad_circles()
        restart = False

    # keys = pygame.key.get_pressed()
    redraw_game_window()

pygame.quit()

# pos = [[50, 50], [150, 150], [250, 250], [350, 350], [450, 450], [50, 150], [50, 250], [50, 350], [50, 450], [150, 50],
#        [150, 250], [150, 350], [150, 450], [250, 50], [250, 150], [250, 350], [250, 450], [350, 50], [350, 150],
#        [350, 250], [350, 450], [450, 50], [450, 150], [450, 250], [450, 350]]