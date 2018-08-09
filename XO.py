import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((500, 350))
pygame.display.set_caption('XO')
clock = pygame.time.Clock()
x = 0
y = 0
xwin = False
owin = False
xturn = True
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
Matrix = [[-1 for x in range(3)] for x in range(3)]
x_axies = [0 for x in range(4)]
y_axies = [0 for x in range(4)]
x_axies[0] = 50
x_axies[1] = 190
x_axies[2] = 320
x_axies[3] = 450
y_axies[0] = 20
y_axies[1] = 100
y_axies[2] = 180
y_axies[3] = 270


def drawX(x_x, x_y):
    pygame.draw.line(gameDisplay, red, (x_x + 21, x_y - 21), (x_x - 21, x_y + 21))
    pygame.draw.line(gameDisplay, red, (x_x - 21, x_y - 21), (x_x + 21, x_y + 21))


def drawO(o_x, o_y):
    pygame.draw.circle(gameDisplay, red, (o_x, o_y), 20, 1)


def xwon():
    if Matrix[0][0] == 0 and Matrix[0][1] == 0 and Matrix[0][2] == 0:
        return True
    elif Matrix[1][0] == 0 and Matrix[1][1] == 0 and Matrix[1][2] == 0:
        return True
    elif Matrix[2][0] == 0 and Matrix[2][1] == 0 and Matrix[2][2] == 0:
        return True
    elif Matrix[0][0] == 0 and Matrix[1][0] == 0 and Matrix[2][0] == 0:
        return True
    elif Matrix[0][1] == 0 and Matrix[1][1] == 0 and Matrix[2][1] == 0:
        return True
    elif Matrix[0][2] == 0 and Matrix[1][2] == 0 and Matrix[2][2] == 0:
        return True
    elif Matrix[0][0] == 0 and Matrix[1][1] == 0 and Matrix[2][2] == 0:
        return True
    elif Matrix[2][0] == 0 and Matrix[1][1] == 0 and Matrix[0][2] == 0:
        return True
    else:
        return False


def owon():
    if Matrix[0][0] == 1 and Matrix[0][1] == 1 and Matrix[0][2] == 1:
        return True
    elif Matrix[1][0] == 1 and Matrix[1][1] == 1 and Matrix[1][2] == 1:
        return True
    elif Matrix[2][0] == 1 and Matrix[2][1] == 1 and Matrix[2][2] == 1:
        return True
    elif Matrix[0][0] == 1 and Matrix[1][0] == 1 and Matrix[2][0] == 1:
        return True
    elif Matrix[0][1] == 1 and Matrix[1][1] == 1 and Matrix[2][1] == 1:
        return True
    elif Matrix[0][2] == 1 and Matrix[1][2] == 1 and Matrix[2][2] == 1:
        return True
    elif Matrix[0][0] == 1 and Matrix[1][1] == 1 and Matrix[2][2] == 1:
        return True
    elif Matrix[2][0] == 1 and Matrix[1][1] == 1 and Matrix[0][2] == 1:
        return True
    else:
        return False


while not (xwin or owin):
    pygame.draw.line(gameDisplay, white, (50, 20), (450, 20))
    pygame.draw.line(gameDisplay, white, (50, 270), (450, 270))
    pygame.draw.line(gameDisplay, white, (50, 20), (50, 270))
    pygame.draw.line(gameDisplay, white, (450, 20), (450, 270))
    pygame.draw.line(gameDisplay, white, (190, 20), (190, 270))
    pygame.draw.line(gameDisplay, white, (320, 20), (320, 270))
    pygame.draw.line(gameDisplay, white, (50, 100), (450, 100))
    pygame.draw.line(gameDisplay, white, (50, 188), (450, 188))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x_axies[3] > x > x_axies[2]:
                if y_axies[3] > y > y_axies[2]:
                    if Matrix[2][2] == -1:
                        if xturn:
                            drawX(385, 225)
                            xturn = False
                            Matrix[2][2] = 0
                        else:
                            drawO(385, 225)
                            xturn = True
                            Matrix[2][2] = 1
                elif y_axies[2] > y > y_axies[1]:
                    if Matrix[2][1] == -1:
                        if xturn:
                            drawX(385, 140)
                            xturn = False
                            Matrix[2][1] = 0
                        else:
                            drawO(385, 140)
                            xturn = True
                            Matrix[2][1] = 1
                elif y_axies[1] > y > y_axies[0]:
                    if Matrix[2][0] == -1:
                        if xturn:
                            drawX(385, 60)
                            xturn = False
                            Matrix[2][0] = 0
                        else:
                            drawO(385, 60)
                            xturn = True
                            Matrix[2][0] = 1
            elif x_axies[2] > x > x_axies[1]:
                if y_axies[3] > y > y_axies[2]:
                    if Matrix[1][2] == -1:
                        if xturn:
                            drawX(250, 225)
                            xturn = False
                            Matrix[1][2] = 0
                        else:
                            drawO(250, 225)
                            xturn = True
                            Matrix[1][2] = 1
                elif y_axies[2] > y > y_axies[1]:
                    if Matrix[1][1] == -1:
                        if xturn:
                            drawX(250, 140)
                            xturn = False
                            Matrix[1][1] = 0
                        else:
                            drawO(250, 140)
                            xturn = True
                            Matrix[1][1] = 1
                elif y_axies[1] > y > y_axies[0]:
                    if Matrix[1][0] == -1:
                        if xturn:
                            drawX(250, 60)
                            xturn = False
                            Matrix[1][0] = 0
                        else:
                            drawO(250, 60)
                            xturn = True
                            Matrix[1][0] = 1
            elif x_axies[1] > x > x_axies[0]:
                if y_axies[3] > y > y_axies[2]:
                    if Matrix[0][2] == -1:
                        if xturn:
                            drawX(120, 225)
                            xturn = False
                            Matrix[0][2] = 0
                        else:
                            drawO(120, 225)
                            xturn = True
                            Matrix[0][2] = 1
                elif y_axies[2] > y > y_axies[1]:
                    if Matrix[0][1] == -1:
                        if xturn:
                            drawX(120, 140)
                            xturn = False
                            Matrix[0][1] = 0
                        else:
                            drawO(120, 140)
                            xturn = True
                            Matrix[0][1] = 1
                elif y_axies[1] > y > y_axies[0]:
                    if Matrix[0][0] == -1:
                        if xturn:
                            drawX(120, 60)
                            xturn = False
                            Matrix[0][0] = 0
                        else:
                            drawO(120, 60)
                            xturn = True
                            Matrix[0][0] = 1
    xwin = xwon()
    owin = owon()
    pygame.display.update()
    clock.tick(20)
if xwin:
    print('x won')
if owin:
    print('o won')
pygame.quit()
quit()
