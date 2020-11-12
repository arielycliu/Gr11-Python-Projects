"""

BLIP THE CIRCLES
Ariel and Janice Game

~Game Instructions~
Click blue circles to collect points
Score streaks by collecting in succession
If a red circles are the enemies, if they touch a blue circle the point and streak is lost
Collect less points than the red circles and you lose a life
Enemies get faster every round, You only have 3 lives

"""

import pygame
import random
import math

pygame.init()

# Creating a window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jan and Ari")

largeFont = pygame.font.SysFont("courier", 40)
medFont = pygame.font.SysFont("courier", 30)
smallFont = pygame.font.SysFont("courier", 20)

restart = True
running = True
delay = 2
speed = delay / 25
start = True

# all possible positions for the circles on a five by five grid
pos = [(50, 50), (150, 150), (250, 250), (350, 350), (450, 450), (50, 150), (50, 250), (50, 350), (50, 450), (150, 50),
       (150, 250), (150, 350), (150, 450), (250, 50), (250, 150), (250, 350), (250, 450), (350, 50), (350, 150),
       (350, 250), (350, 450), (450, 50), (450, 150), (450, 250), (450, 350)]
goodCircles = []
badCircles = []
score = 0
roundScore = 0
jojoScore = 0
firstRound = True
round = 1
streak = 0
life = 3


class Circle(object):
    def __init__(self, color, center, radius):
        self.color = color
        self.center = center
        self.radius = radius
        self.closest = 1  # used for bad circles only, saves index of circle it's heading towards

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.center, self.radius)


def redraw_game_window():
    win.fill(000)

    lives = smallFont.render("Lives: " + str(life), True, (255, 255, 255))
    win.blit(lives, (10, 10))

    scores = smallFont.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(scores, (350, 10))

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


def intro_screen():
    win.fill(000)
    pygame.display.update()

    # this is to start off the program

    story = ["~Welcome to Return of the JoJos~", "You're a scientist", "from galaxy Sinusoidal-Costangent",
             "where apples can't float...", "You have come to Earth-DJ6 on a mission.",
             "Take as many good humans as possible,", "and research their capabilities", "but we have an issue...",
             "Jojos are also taking humans", "using them to solve math problems", "Who will win...",
             "and capture the most humans?", "END"]

    start_screen = True
    while start_screen:

        pygame.time.delay(100)

        for s in story:

            if s == "END":  # like reading end of file
                return
            space_skip = smallFont.render("Space to skip", True, (255, 255, 255))
            win.blit(space_skip, (25, 450))
            click_skip = smallFont.render("Click to advance", True, (255, 255, 255))
            win.blit(click_skip, (280, 450))
            text_display_1 = smallFont.render(s, True, (255, 255, 255))
            win.blit(text_display_1, (250 - (text_display_1.get_width() / 2), 250 - (text_display_1.get_height() / 2)))
            print(s)

            pygame.display.update()
            reading = True

            while reading is True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # check quit game
                        global running
                        running = False
                        return
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        return
                    if event.type == pygame.MOUSEBUTTONUP:  # check clicking
                        win.fill(000)
                        reading = False
                        break


def menu():
    menu_screen = True
    while menu_screen:

        pygame.time.delay(100)
        win.fill(000)

        space_skip = smallFont.render("Press space to play", True, (255, 255, 255))
        win.blit(space_skip, (250, 450))

        game_title = largeFont.render("RETURN OF THE JOJO", True, (255, 255, 255))
        win.blit(game_title, (35, 100))

        play_title = largeFont.render("How to play", True, (255, 255, 255))
        win.blit(play_title, (120, 200))
        pygame.draw.rect(win, (255, 255, 255), (75, 200, 350, 50), 3)

        play_title = largeFont.render("PLAY", True, (255, 255, 255))
        win.blit(play_title, (200, 315))
        pygame.draw.rect(win, (255, 255, 255), (150, 300, 200, 75), 3)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check quit game
                global running
                running = False
                menu_screen = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                menu_screen = False
            if event.type == pygame.MOUSEBUTTONUP:  # check clicking
                pos = pygame.mouse.get_pos()
                x, y = pos

                # check if how to play
                if x >= 75 and x <= 425 and y >= 200 and y <= 250:
                    how_to_play()
                    win.fill(000)
                    pygame.display.update()

                # check if play
                if x >= 150 and x <= 350 and y >= 300 and y <= 375:
                    win.fill(000)
                    pygame.display.update()
                    return


def how_to_play():
    print("How to Play:")
    win.fill(000)
    pygame.display.update()

    # this is to start off the program
    print("Program start!")

    instructions = ["~Game Instructions~", "Collect the blue humans", "Click blue circles to collect",
                    "Score points by collecting", "Score streaks by collecting in succession",
                    "If a red (Jojo) touches a blue",
                    "that point and streak is lost", "Collect less points than red", "and you lose a life",
                    "Enemies get faster every round",
                    "You only have 3 lives", "Collect the humans before JOJO!", "Who will win...",
                    "and capture the most humans?", "END"]

    help_screen = True
    while help_screen:

        pygame.time.delay(100)

        for s in instructions:

            if s == "END":
                return
            space_skip = smallFont.render("Space to return", True, (255, 255, 255))
            win.blit(space_skip, (25, 450))
            click_skip = smallFont.render("Click to advance", True, (255, 255, 255))
            win.blit(click_skip, (280, 450))
            text_display_1 = smallFont.render(s, True, (255, 255, 255))
            win.blit(text_display_1, (250 - (text_display_1.get_width() / 2), 250 - (text_display_1.get_height() / 2)))
            print(s)

            pygame.display.update()
            reading = True

            while reading is True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # check quit game
                        global running
                        running = False
                        return
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        return
                    if event.type == pygame.MOUSEBUTTONUP:  # check clicking
                        win.fill(000)
                        reading = False
                        break


def endscreen():
    global restart, goodCircles, badCircles, round, speed, score, roundScore, jojoScore, life, running, streak
    win.fill(000)
    pygame.display.update()
    restart = True

    if roundScore >= jojoScore:

        end = True
        while end:

            pygame.time.delay(100)

            roundText = largeFont.render("Round " + str(round) + " Over:", True, (255, 255, 255))
            rudeTexxt = medFont.render("Round score is " + str(roundScore), True, (255, 255, 255))
            rudeTextt = medFont.render("Total score is " + str(score), True, (255, 255, 255))
            moreTexts = medFont.render("Jojo's score is " + str(jojoScore), True, (255, 255, 255))
            nextRound = smallFont.render("Press space to enter next round", True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # check quit game
                    global running
                    running = False
                    return
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                end = False

            win.blit(roundText, (30, 75))
            win.blit(rudeTexxt, (30, 150))
            win.blit(rudeTextt, (30, 225))
            win.blit(moreTexts, (30, 300))
            win.blit(nextRound, (60, 400))
            pygame.display.update()

        # updating all the variables
        jojoScore = 0
        roundScore = 0

        round += 1
        speed += delay / 100

    else:
        life -= 1
        score -= roundScore

        if life == 0:
            game_over()
            score = 0
            roundScore = 0
            jojoScore = 0
            round = 1
            streak = 0
            speed = delay / 25
            life = 3
            return

        end = True
        while end:
            pygame.time.delay(100)

            roundText = largeFont.render("YOU LOST A LIFE", True, (255, 255, 255))
            rudeTexxt = smallFont.render("Round score is " + str(roundScore), True, (255, 255, 255))
            rudeTextt = smallFont.render("Total score is " + str(score), True, (255, 255, 255))
            moreTexts = smallFont.render("Jojo's score is " + str(jojoScore), True, (255, 255, 255))
            play_again = largeFont.render("Redo the level", True, (255, 255, 255))
            nextRound = smallFont.render("Press space to continue playing", True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # check quit game
                    running = False
                    return
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                end = False

            win.blit(roundText, (30, 50))
            win.blit(rudeTexxt, (30, 110))
            win.blit(rudeTextt, (30, 140))
            win.blit(moreTexts, (30, 170))
            win.blit(play_again, (30, 250))
            win.blit(nextRound, (30, 400))
            pygame.display.update()

        win.fill(000)
        pygame.display.update()

        roundScore = 0
        jojoScore = 0


def game_over():
    pygame.mixer.music.set_volume(0.3)
    global score, running

    file = open("highscores.txt", "r")

    initials = []
    hscores = []

    for i in range(10):
        initial = file.readline()
        initials.append(initial)

        hscore = file.readline()
        hscores.append(hscore)

    # closes the file to write to it later
    file.close()

    win.fill(000)

    game_over_screen = True
    while game_over_screen:

        roundText = largeFont.render("GAME OVER", True, (255, 255, 255))

        rudeTextt = medFont.render("Total score is: " + str(score), True, (255, 255, 255))
        space_skip = smallFont.render("Press space to play again!", True, (255, 255, 255))

        win.blit(roundText, (30, 50))
        win.blit(rudeTextt, (30, 200))
        win.blit(space_skip, (180, 450))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check quit game
                global running
                running = False
                return
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                win.fill(000)
                pygame.display.update()
                game_over_screen = False

        score_is_a_highscore = False
        for hscore in hscores:  # scans from top to bottom to check if the score is a highscore
            if score >= int(hscore):
                score_is_a_highscore = True
                scoreRank = hscores.index(hscore)
                break

        if score_is_a_highscore:
            if scoreRank == 9:
                pass
            else:
                try:
                    for i in range(1, 10): # moves everything down to insert the new highscore
                        hscores[scoreRank], hscores[scoreRank + i] = hscores[scoreRank + i], hscores[scoreRank]
                        initials[scoreRank], initials[scoreRank + i] = initials[scoreRank + i], initials[scoreRank]
                except:
                    pass # this means that all values have been pushed down by 1

            hscores[scoreRank] = str(score) + "\n"

            print("Congrats: High score!")

            high_score_screen = True
            userInit = ""
            while high_score_screen:
                while len(userInit) != 3:  # once the initials are set they are unchangeable, similar to arcade games
                    win.fill(000)
                    roundText = largeFont.render("GAME OVER", True, (255, 255, 255))
                    high_score = largeFont.render("HIGH SCORE", True, (255, 255, 255))
                    rudeTextt = medFont.render("Total score is: " + str(score), True, (255, 255, 255))
                    username = medFont.render("Input username: ", True, (255, 255, 255))
                    userNAME = medFont.render(userInit, True, (255, 255, 255))
                    space_skip = smallFont.render("Press space to play again!", True, (255, 255, 255))

                    win.blit(roundText, (30, 50))
                    win.blit(high_score, (30, 90))
                    win.blit(rudeTextt, (30, 200))
                    win.blit(username, (30, 300))
                    win.blit(userNAME, (330, 300))
                    win.blit(space_skip, (180, 450))

                    pygame.display.update()

                    # takes the user
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                userInit = userInit[:-1]
                            if event.unicode.isalpha():
                                userInit += event.unicode.upper()
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_SPACE]:
                                win.fill(000)
                                pygame.display.update()
                                return

                        pygame.display.update()

                userNAME = medFont.render(userInit, True, (255, 255, 255))
                win.blit(userNAME, (330, 300))
                pygame.display.update()

                print("The previous highscores were:")
                for i in range(10):
                    print(str((i + 1)) + ". " + initials[i][:3] + ", " + str(hscores[i]))

                initials[scoreRank] = userInit + "\n"

                # makes the file blank
                file = open("highscores.txt", "w")

                # now we put the new data back into the file
                insertString = ""
                for i in range(10):
                    insertString += initials[i]
                    insertString += str(hscores[i])

                file.write(insertString)
                file.close()

                while True:  # makes player choose to quit or play again
                    pygame.time.delay(100)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_SPACE]:
                            win.fill(000)
                            pygame.display.update()
                            return


def circle_find():
    global goodCircles, badCircles

    for circle in badCircles:
        # find distance between bad circles and good circles
        distance = []

        for goodCirc in goodCircles:
            distance.append(
                math.sqrt((circle.center[0] - goodCirc.center[0]) ** 2 + (circle.center[1] - goodCirc.center[1]) ** 2))

        # closest circle center coords passed to badCircs
        closest = goodCircles[distance.index(min(distance))].center
        circle.closest = distance.index(
            min(distance))  # saves the index of the closest circle to delete the circle later
        distance = min(distance)  # fetches the lowest distance

        # movement - calculated using similar triangle ratios
        if not closest[0] - circle.center[0] == 0:  # checks to see if it is vertically aligned
            circle.center = (circle.center[0] + speed * (closest[0] - circle.center[0]) / abs(distance),
                             circle.center[1] + speed * (closest[1] - circle.center[1]) / abs(distance))

        else:  # this just moves it up and down
            if closest[1] > circle.center[1]:
                circle.center = (circle.center[0], circle.center[1] + speed)
            if closest[1] < circle.center[1]:
                circle.center = (circle.center[0], circle.center[1] - speed)


def get_hit(index):
    global jojoScore, goodCircles, streak
    goodCircles.pop(index)  # removes the hit circle
    jojoScore += 5
    streak = 0  # breaks any streak


running = True

# this is to start off the program
print("Program start!")

while running:
    if start == True:
        pygame.mixer.music.load('ghost_choir.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        intro_screen()
        menu()
        pygame.mixer.music.set_volume(1)
        start = False

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
                    roundScore += 5 * (streak // 3 + 1)
                    score += 5 * (streak // 3 + 1)

    # to check if the bad circle has touched the good circle
    for circle in badCircles:
        try:  # for when an enemy tries to delete an circle that is already gone
            xb, yb = circle.center
            xg, yg = goodCircles[circle.closest].center
        except:
            continue
        distance = math.hypot(xb - xg, yb - yg)  # calculate distance
        if distance <= 2 * circle.radius:  # compare distance of click from center of circle to radius of circle
            get_hit(circle.closest)

    if goodCircles == [] and firstRound == False:  # otherwise round screen would display right after the menu
        endscreen()
    elif goodCircles == [] and firstRound == True:
        firstRound = False

    if restart == True:
        pos = [(50, 50), (150, 150), (250, 250), (350, 350), (450, 450), (50, 150), (50, 250), (50, 350), (50, 450),
               (150, 50), (150, 250), (150, 350), (150, 450), (250, 50), (250, 150), (250, 350), (250, 450), (350, 50),
               (350, 150), (350, 250), (350, 450), (450, 50), (450, 150), (450, 250), (450, 350)]
        goodCircles = []
        badCircles = []
        create_good_circles()
        create_bad_circles()
        restart = False

    try:
        circle_find()
    except:  # for when circles are removed at simultaneous times or other similar errors
        pass

    redraw_game_window()

    pygame.time.delay(delay)  # rate

pygame.quit()
