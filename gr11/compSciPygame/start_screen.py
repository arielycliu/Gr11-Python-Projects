import pygame
import random
import math

pygame.init()

# Creating a window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jan and Ari Game")

restart = True


largeFont = pygame.font.SysFont("courier", 40)
smallFont = pygame.font.SysFont("courier", 20)




def intro_screen():

    win.fill(000)
    pygame.display.update()

    # this is to start off the program
    print("Program start!")

    story = ["~Welcome to Return of the JoJos~", "You're a scientist", "from galaxy Sinusoidal-Costangent",
             "where apples can't float...", "You have come to Earth-DJ6 on a mission",
             "Take as many good humans as possible,", "and research their capabilities", "but we have an issue...",
             "Jojos are also taking humans", "using them to solve math problems", "Who will win...",
             "and capture the most humans?", "END"]

    start_screen = True
    while start_screen:

        pygame.time.delay(100)

        for s in story:

            if s == "END":
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
                    if event.type == pygame.MOUSEBUTTONUP: # check clicking
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
        pygame.draw.rect(win, (255,255,255), (75, 200, 350, 50), 3)

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
             "Score points by collecting", "Score streaks by collecting in succession",  "If a red (Jojo) touches a blue",
            "that point is lost", "Collect less points than red", "and you lose a life", "Enemies get faster every roung",
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

intro_screen()
menu()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check quit game
            running = False

    intro_screen()
    menu()

    game_title = largeFont.render("BLIP", True, (255, 255, 255))
    win.blit(game_title, (200, 100))

    pygame.time.delay(25)  # rate

pygame.quit()
