import pygame

pygame.init()

y2 = 0
sp = 0
epY = 0
epX = 0
hold = False
cut = False
win = False

screen = pygame.display.set_mode((1280,720), vsync=1)
pygame.mouse.set_visible(0)
pygame.display.set_caption("cutting game")
pygame.display.set_icon(pygame.image.load("knife_icon.png").convert_alpha())

boxes = [pygame.image.load("box1.png").convert_alpha(),
         pygame.image.load("box2.png").convert_alpha(),
         pygame.image.load("box3.png").convert_alpha(),
         pygame.image.load("box4.png").convert_alpha(),
         pygame.image.load("box5.png").convert_alpha()]
boxnum = 1

CPO = pygame.image.load("cutting part overlay.png").convert_alpha()

cursor = pygame.image.load("knife.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (200, 200))

text = "cutting game"
titlefont = pygame.font.SysFont('Arial', 100, True)
fpsfont = pygame.font.SysFont('Arial', 20, True)

win_icon = pygame.image.load("win_icon.png").convert_alpha()

clock = pygame.time.Clock()

running = True
while running == True:
    screen.fill((100, 255, 100))
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    if hold == False:
        y2 = y
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            hold = True
            spX, spY = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            hold = False
            cut = True
    if hold == True:
        screen.fill((255, 0, 0))
    if win == False:
        screen.blit(boxes[boxnum-1], (390, 550))
    if hold == True: 
        epX, epY = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0, 0, 0), (spX, spY), (epX, spY))        
    if cut == True and win == False:
        if boxnum == 1:
            if epX < 405 and spX > 870 or epX > 870 and spX < 405:
                if spY > 570 and spY < 595:
                    text = "good cut"
                    cut = False
                    boxnum = 2
                else:
                    text = "bad cut"
                    cut = False
            else:
                text = "bad cut"
                cut = False
        elif boxnum == 2:
            if epX < 407 and spX > 872 or epX > 872 and spX < 407:
                if spY > 570 and spY < 590:
                    text = "good cut"
                    cut = False
                    boxnum = 3
                else:
                    text = "bad cut"
                    cut = False
                    boxnum = 1
            else:
                text = "bad cut"
                cut = False
                boxnum = 1
        elif boxnum == 3:
            if epX < 408 and spX > 868 or epX > 868 and spX < 408:
                if spY > 290 and spY < 590:
                    text = "good cut"
                    cut = False
                    boxnum = 4
                else:
                    text = "bad cut"
                    cut = False
                    boxnum = 1
            else:
                text = "bad cut"
                cut = False
                boxnum = 1
        elif boxnum == 4:
            if epX < 410 and spX > 869 or epX > 869 and spX < 410:
                if spY > 580 and spY < 585:
                    text = "good cut"
                    cut = False
                    boxnum = 5
                else:
                    text = "bad cut"
                    cut = False
                    boxnum = 1
            else:
                text = "bad cut"
                cut = False
                boxnum = 1
        elif boxnum == 5:
            if epX < 412 and spX > 868 or epX > 868 and spX < 412:
                if spY > 579 and spY < 583:
                    text = "game won"
                    cut = False
                    win = True
                else:
                    text = "bad cut"
                    cut = False
                    boxnum = 1
            else:
                text = "bad cut"
                cut = False
                boxnum = 1
    if hold == True:
        screen.blit(CPO, (0, 0))
    screen.blit(cursor, (x, y2))
    if win == True:
        screen.blit(win_icon, (385, 150))
    textrect = titlefont.render(text, True, (255, 255, 255))
    text_pos = textrect.get_rect(center=(640, 70))
    screen.blit(textrect, text_pos)
    screen.blit(fpsfont.render(str(round(clock.get_fps())), True, (255, 255, 255)), (5, 4))
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get(pygame.QUIT):
        running = False
        pygame.quit()
