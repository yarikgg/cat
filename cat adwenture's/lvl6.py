f = open('lvl.txt', 'r')
chek = f.read()
f.close()


if chek == '6':
    import pygame
    import time
    pygame.init()
    w, h = 800, 402
    display = pygame.display.set_mode((w, h))
    # спрайты
    cat = pygame.image.load('cat.png')
    cat_animation1 = pygame.image.load('cat_animation1.png')
    cat_animation2 = pygame.image.load('cat_animation2.png')
    final_animation = pygame.image.load('cat_animation_final.png')
    bat = pygame.image.load('bat.png')
    lvl1 = pygame.image.load('lvl6.png')
    mouse = pygame.image.load('mouse.png')
    enemy = pygame.image.load('неадекват.png')
    enemy2 = pygame.image.load('неадекват2.png')
    fire_ball = pygame.image.load('fire ball.png')
    menu = pygame.image.load('menu.png')
    # переменные
    x = 0
    catx = 30
    caty = 315

    mx = 600

    bx = 250

    stopmouse = True

    kx = 250

    fx1 = 0
    fx2 = 750

    i = 2

    FPS = 60

    jump = False
    game = True
    start = True

    health = 3
    # гравитация для пола

    def graviti():
        global caty
        global catx
        if caty <= 340:
            caty += 2
            if caty >= 340:
                caty = 340
    # гравитация для "мостика"

    # отрисовка стартовой позиции- не обязательно
    display.blit(lvl1, (0, 0))
    display.blit(cat, (catx, caty))
    pygame.display.update()

    clock = pygame.time.Clock()

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if game == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        x = 1
                    if event.key == pygame.K_LEFT:
                        x = -1
                    if event.key == pygame.K_SPACE:
                        if caty == 340:
                            jump = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        x = 0
                    if event.key == pygame.K_LEFT:
                        x = 0
                    if event.key == pygame.K_SPACE:
                        jump = False
            elif game == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                    x, y = pygame.mouse.get_pos()
                    if x >= 312 and y >= 111:
                        if x <= 495 and y <= 160:
                            game = True
        if game == True:
            f = pygame.font.SysFont('serif', 48)  # текст
            text = f.render('здоровье='+str(health), True,
                            (0, 180, 0))
            clock.tick(FPS)
            # основная логика
            if x == 1:
                catx += 2
            if x == -1:
                catx -= 2
            if jump == True:
                display.blit(lvl1, (0, 0))  # анимация
                display.blit(cat_animation1, (catx, caty))
                display.blit(text, (4, 4))
                display.blit(fire_ball, (fx1, 350))
                display.blit(fire_ball, (fx2, 350))
                display.blit(enemy, (750, 350))
                display.blit(enemy2, (0, 350))  # анимация
                pygame.display.update()  # анимация
                time.sleep(0.3)
                fx1 += 20
                fx2 -= 20  # анимация
                display.blit(lvl1, (0, 0))  # анимация
                display.blit(cat_animation2, (catx, caty))
                display.blit(text, (4, 4))
                display.blit(fire_ball, (fx1, 350))
                display.blit(fire_ball, (fx2, 350))
                display.blit(enemy, (750, 350))
                display.blit(enemy2, (0, 350))  # анимация
                pygame.display.update()  # анимация
                time.sleep(0.3)
                display.blit(lvl1, (0, 0))
                caty -= 160
                catx += 60
                fx1 += 20
                fx2 -= 20
                display.blit(final_animation, (catx, caty))
                display.blit(text, (4, 4))
                display.blit(fire_ball, (fx1, 350))
                display.blit(fire_ball, (fx2, 350))
                display.blit(enemy, (750, 350))
                display.blit(enemy2, (0, 350))
                pygame.display.update()
                jump = False
            bx -= 1
            if catx >= 0:
                graviti()
            if catx >= 800:
                print('ты выйграл')
                f = open('lvl.txt', 'w')
                f.write('7')
                f.close()
                time.sleep(3)
                exit()
            if catx >= 316 and catx <= 372 and caty == 184:  # проверка наступил ли игрок на лужу
                start = False
            fx1 += 2
            fx2 -= 2
            if fx1 == 800:
                fx1 = 0
                fx2 = 750
            if fx1 == catx and caty >= 320:
                health -= 1
            if fx2 == catx and caty >= 320:
                health -= 1.5
            if health <= 0:
                game = False
            if catx >= 187 and catx <= 270 and caty == 340:
                health -= 1
            # отрисовка ВСЕХ обьетов
            pygame.display.update()
            display.blit(lvl1, (0, 0))
            display.blit(cat, (catx, caty))
            display.blit(text, (4, 4))
            display.blit(fire_ball, (fx1, 350))
            display.blit(fire_ball, (fx2, 350))
            display.blit(enemy, (750, 350))
            display.blit(enemy2, (0, 350))
            pygame.display.update()
        elif game == False:
            catx = 30
            caty = 315
            display.blit(menu, (0, 0))
            pygame.display.update()
else:
    print('пройдите 5 уровень!')
