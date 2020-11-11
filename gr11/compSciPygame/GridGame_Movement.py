import pygame
import random
import math

pygame.init()

# Creating a window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jan and Ari Mack a Mole")

restart = True

speed = 1

class Circle(object):
    def __init__(self, color, center, radius):
        self.color = color
        self.center = center
        self.radius = radius
        self.closest = 1 # used for bad circles only, saves index of circle it's heading towards

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
    num_of_circles = 6
    size = 23
    for i in range(num_of_circles):
        coord = random.choice(pos)  # choose a random location
        pos.remove(coord)  # Remove that possible spot
        goodCircles.append(Circle((164, 213, 208), coord, size))
        # if round over then restart pos# code to create instances of the object


def create_bad_circles():
    num_of_circles = 3
    size = 23
    for i in range(num_of_circles):
        coord = random.choice(pos)  # choose a random location
        pos.remove(coord)  # Remove that possible spot
        badCircles.append(Circle((255, 25, 58), coord, size))
        # if round over then restart pos# code to create instances of the object


def endscreen():
    global restart, goodCircles, badCircles, round, speed
    restart = True
    print("HMMMM")

    goodCircles = []
    badCircles = []

    round += 1
    speed += 0.25

    win.fill(000)
    pygame.display.update()

    roundText = largeFont.render("Round " + str(round) + " Over:", True, (255, 255, 255))
    rudeTextt = largeFont.render("your score is " + str(score), True, (255, 255, 255))
    moreTexts = largeFont.render("Jojo's score is " + str(jojoScore), True, (255, 255, 255))
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

        win.blit(roundText, (30, 150))
        win.blit(rudeTextt, (40, 225))
        win.blit(moreTexts, (30, 300))
        win.blit(nextRound, (60, 400))
        pygame.display.update()

def circle_find():
    global goodCircles, badCircles

    for circle in badCircles:
        # find distance between bad circles and good circles
        distance = []

        for goodCirc in goodCircles:
            distance.append(math.sqrt((circle.center[0] - goodCirc.center[0]) ** 2 + (circle.center[1] - goodCirc.center[1]) ** 2))

        # closest circle center coords passed to badCircs
        closest = goodCircles[distance.index(min(distance))].center
        circle.closest = distance.index(min(distance)) # saves the index of the closest circle to delete the circle later
        distance = min(distance) # fetches the lowest distance

        # movement
        if not closest[0] - circle.center[0] == 0: # checks to see if it is vertically aligned
            circle.center = (circle.center[0] + speed * (closest[0] - circle.center[0]) / abs(distance), circle.center[1] + speed * (closest[1] - circle.center[1]) / abs(distance))

        else: # this just moves it up and down
            if closest[1] > circle.center[1]:
                circle.center = (circle.center[0], circle.center[1] + speed)
            if closest[1] < circle.center[1]:
                circle.center = (circle.center[0], circle.center[1] - speed)

def get_hit(index):
    global jojoScore, goodCircles, streak
    goodCircles.pop(index)
    print('hit')
    jojoScore += 5
    streak = 0

# all possible positions for the circles on a five by five grid
pos = [(50, 50), (150, 150), (250, 250), (350, 350), (450, 450), (50, 150), (50, 250), (50, 350), (50, 450), (150, 50), (150, 250), (150, 350), (150, 450), (250, 50), (250, 150), (250, 350), (250, 450), (350, 50), (350, 150), (350, 250), (350, 450), (450, 50), (450, 150), (450, 250), (450, 350)]
goodCircles = []
badCircles = []
score = 0
jojoScore = 0
round = 0
streak = 0

running = True

# this is to start off the program
print("Program start!")
print("We\'ll put more things in here later don't worry")
print("btw I added a streak function")

largeFont = pygame.font.SysFont("courier", 40)
smallFont = pygame.font.SysFont("courier", 20)

startTitle = largeFont.render("~Welcome to Return of the JoJos~", True, (255, 255, 255))
startInfo1 = smallFont.render("You come from the galaxy called Sinusoidal", True, (255, 255, 255))
startInfo2 = smallFont.render("Costangent where apples can't float.", True, (255, 255, 255))
startInfo3 = smallFont.render("You have come to Earth-1ODJ6 on a research", True, (255, 255, 255))
startInfo4 = smallFont.render("mission to take as many good humans as possible,", True, (255, 255, 255))
startInfo5 = smallFont.render("while protecting them from the bad Jojos", True, (255, 255, 255))
startInfo6 = smallFont.render("who want to use them to solve math problems.", True, (255, 255, 255))


win.blit(startInfo1, (30, 150))
win.blit(startInfo1, (40, 225))
win.blit(startInfo1, (30, 300))
win.blit(startInfo1, (60, 400))

pygame.display.update()

while running:

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

                    streak += 1
                    score += 5 * (streak // 3 + 1)

    # to check if the bad circle has touched the good circle
    for circle in badCircles:
        try: # for when an enemy tries to delete an circle that is already gone
            xb, yb = circle.center
            xg, yg = goodCircles[circle.closest].center
        except:
            continue
        distance = math.hypot(xb - xg, yb - yg)  # calculate distance
        if distance <= 2 * circle.radius:  # compare distance of click from center of circle to radius of circle
            get_hit(circle.closest)

    if goodCircles == []:
        endscreen()

    if restart == True:
        pos = [(50, 50), (150, 150), (250, 250), (350, 350), (450, 450), (50, 150), (50, 250), (50, 350), (50, 450), (150, 50), (150, 250), (150, 350), (150, 450), (250, 50), (250, 150), (250, 350), (250, 450), (350, 50), (350, 150), (350, 250), (350, 450), (450, 50), (450, 150), (450, 250), (450, 350)]
        goodCircles = []
        badCircles = []
        create_good_circles()
        create_bad_circles()
        restart = False

    try:
        circle_find()
    except:
        pass

    redraw_game_window()

    pygame.time.delay(25)  # rate

pygame.quit()
