f = open('lvl.txt', 'r')
chek = f.read()
f.close()

if chek == '4':
    import pygame
    import time


    w,h = 800,402
    display = pygame.display.set_mode((w,h))

    cat = pygame.image.load('cat.png')
    cat_animation1 = pygame.image.load('cat_animation1.png') 
    cat_animation2 = pygame.image.load('cat_animation2.png')
    final_animation = pygame.image.load('cat_animation_final.png')
    lvl1 = pygame.image.load('lvl4.png')
    mouse = pygame.image.load('mouse.png')
    chert = pygame.image.load('неадекват.png')
    fire_ball = pygame.image.load('fire ball.png')

    x = 0
    catx = 30
    caty = 300

    mx = 600

    fx=550

    stopmouse = True

    i = 2

    health = 3

    def graviti():
        global caty
        global catx
        if caty < 325:
            caty += 2
            if caty >= 325:
                caty = 325 

    def graviti2():
        global caty
        global catx
        graviti = False
        if caty < 261:
            caty += 2
            if caty >= 261:
                caty = 261 

    display.blit(lvl1,(0,0))
    display.blit(cat,(catx,caty))
    pygame.display.update()

    clock = pygame.time.Clock()

    FPS = 60

    jump = False

    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x = 1
                if event.key == pygame.K_LEFT:
                    x = -1
                if event.key == pygame.K_SPACE:
                    jump = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x = 0
                if event.key == pygame.K_LEFT:
                    x = 0
                if event.key == pygame.K_SPACE:
                    jump = False

        clock.tick(FPS)
        if x == 1:
            catx += 2
        if x == -1:
            catx -= 2
        if jump == True:
            display.blit(lvl1,(0,0))                        #   анимация
            display.blit(cat_animation1,(catx,caty))  
            display.blit(mouse,(mx, 287))   
            display.blit(chert,(550, 250))
            fx-=10
            display.blit(fire_ball,(fx, 260))   #   анимация
            pygame.display.update()                         #   анимация   
            time.sleep(0.3)                                 #   анимация
            display.blit(lvl1,(0,0))                        #   анимация
            display.blit(cat_animation2,(catx,caty))
            display.blit(mouse,(mx, 287))
            display.blit(chert,(550, 250)) 
            fx -= 10
            display.blit(fire_ball,(fx, 260))       #   анимация       
            pygame.display.update()                         #   анимация
            time.sleep(0.3)
            display.blit(lvl1,(0,0))
            caty -= 140
            catx += 100
            display.blit(final_animation,(catx,caty))
            display.blit(mouse,(mx, 287))
            display.blit(chert,(550, 250))
            fx -= 10
            display.blit(fire_ball,(fx, 260))
            pygame.display.update()
            jump = False
        if catx <= 73:
            graviti()
        if catx >= 74 and caty >= 262:
            x = 0
        if catx >= 74:
            graviti2()
        if catx >= 800:
            print('ты выйграл')
            f=open('lvl.txt','w')
            f.write('5')
            f.close()
            time.sleep(3)      
            exit()
        if catx >= 324 and catx <= 451:
            caty += 2
        if catx == 520 and 561 and caty >= 261:
            health -= 1
        if health == 0:
            exit()
        if catx == mx and 610 and jump == False:
            stopmouse = False
            health += 1
        if stopmouse == False:
            mx += 7
        if caty >= 402:
            exit()
        if catx >= 141 and catx <= 240 and caty >= 261:
            health -= 1
        fx-=2
        if fx <= 0:
            fx=550
        if fx == catx and caty == 261:
            start = 0
        display.blit(lvl1,(0,0))        
        display.blit(cat,(catx,caty))    
        display.blit(mouse,(mx, 287)) 
        display.blit(chert,(550, 250))
        display.blit(fire_ball,(fx, 260))
        pygame.display.update()


else:
    print('пройдите 3 уровень')