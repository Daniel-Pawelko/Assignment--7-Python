import pygame
import sys
import math

pygame.init()

black = (0, 0, 0)
WIDTH = 960
HEIGHT = 720
bspeed = 10
mspeed = 3
y1 = 200
x1 = 10
y2 = 500
x2 = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GO TO BED!')
b1 = pygame.image.load('back1.jpg')
b2 = pygame.image.load('back2.jpg')
batImg = pygame.image.load('bat.png')
abbyImg = pygame.image.load('mom.png')
textboxImg = pygame.image.load('textbox.png')


def board(x, y):
    screen.blit(b1, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, x, y):
    largeText = pygame.font.Font('FreeSansBold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    screen.blit(textboxImg, (x, y))
    screen.blit(TextSurf, (x + 25, y + 90))


def bat():
    screen.blit(batImg, (x1, y1))


def mom():
    screen.blit(abbyImg, (x2, y2))


def board2(x, y):
    screen.blit(b2, (x, y))


board(0, 0)
bat()
message_display('bed time', 600, 300)
mom()
pygame.display.update()
pygame.time.wait(1500)
board(0, 0)
bat()
message_display('bed time', 600, 300)
message_display('catch me', 200, 100)
mom()
pygame.display.update()
pygame.time.wait(1500)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # movement
    if event.type == pygame.KEYDOWN:
        print('pressing')
        if event.key == pygame.K_LEFT:
            x1 -= bspeed
        if event.key == pygame.K_RIGHT:
            x1 += bspeed
        if event.key == pygame.K_UP:
            y1 -= bspeed
        if event.key == pygame.K_DOWN:
            y1 += bspeed

    if x1 < x2 and y1 < y2:
        x2 -= mspeed
        y2 -= mspeed
    elif x1 < x2:
        x2 -= mspeed
    elif y1 < y2:
        y2 -= mspeed

    if x1 > x2 and y1 > y2:
        x2 += mspeed
        y2 += mspeed
    elif x1 > x2:
        x2 += mspeed
    elif y1 > y2:
        y2 += mspeed

    distx = math.hypot(x1 - x2)
    disty = math.hypot(y1 - y2)
    if (distx <= 50 or distx <= -50) and (disty <= 50 or disty <= -50):
        print('same')
        break

    # Start here
    board(0, 0)
    bat()
    mom()
    pygame.display.update()

# After caught
for i in range(400):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    print(i)
    # Start Here

    # Mom position
    if x2 < 369:
        x2 += mspeed
    elif x2 > 369:
        x2 -= mspeed

    if y2 < 431:
        y2 += mspeed
    elif y2 > 431:
        y2 -= mspeed

    # Bat position
    if x1 < 190:
        x1 += bspeed
    elif x1 > 190:
        x1 -= bspeed

    if y1 < 200:
        y1 += bspeed
    elif y1 > 200:
        y1 -= bspeed

    board2(0, 0)
    bat()
    mom()
    message_display('GN!', x2 + 50, y2 - 150)
    pygame.display.update()

# Exit
sys.exit()
