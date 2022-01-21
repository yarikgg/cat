f=open('lvl.txt','r')
chek = f.read()
f.close()

if chek == '3':
    import pygame
    import time
    pygame.init()
    w,h = 800,402
    display = pygame.display.set_mode((w,h))

    moster = pygame.image.load('water_monster.png')
    cat = pygame.image.load('cat.png')
    cat_animation1 = pygame.image.load('cat_animation1.png')
    cat_animation2 = pygame.image.load('cat_animation2.png')
    final_animation = pygame.image.load('cat_animation_final.png')
    bat = pygame.image.load('bat.png')
    lvl1 = pygame.image.load('lvl3.png')
    mouse = pygame.image.load('mouse.png')
    dontnormal = pygame.image.load('неадекват.png')
    fire_ball = pygame.image.load('fire ball.png')

    x = 0
    catx = 30
    caty = 300

    mx = 500

    bx = 250

    stopmouse = True

    kx = 114

    nx = 550

    fx = 550
    i = 2

    health = 3

    def graviti():
        global caty
        global catx
        if caty <= 300:
            caty += 2
            if caty >= 300:
                caty = 300

    def graviti2():
        global caty
        global catx
        graviti = False
        if caty <= 238:
            caty += 2
            if caty >= 238:
                caty = 238  

    def graviti3():
        global caty
        global catx
        graviti = False
        if caty <= 176:
            caty += 2
            if caty >= 176:
                caty = 176


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

        f = pygame.font.SysFont('serif', 48)
        text = f.render('здоровье='+str(health), True,
            (0, 180, 0))
        clock.tick(FPS)
        if x == 1:
            catx += 2
        if x == -1:
            catx -= 2
        if jump == True:
            display.blit(lvl1,(0,0))                        #   анимация
            display.blit(cat_animation1,(catx,caty))
            display.blit(text,(4,4))  
            display.blit(moster,(kx,340))
            display.blit(bat,(mx, 250))
            display.blit(dontnormal,(nx, 303))
            display.blit(fire_ball,(fx, 303)) 
            fx -= 10    #   анимация
            pygame.display.update()                         #   анимация   
            time.sleep(0.1)                                 #   анимация
            display.blit(lvl1,(0,0))                        #   анимация
            display.blit(cat_animation2,(catx,caty))
            display.blit(text,(4,4))
            display.blit(moster,(kx,340))
            display.blit(bat,(mx, 250))
            display.blit(dontnormal,(nx, 303))
            display.blit(fire_ball,(fx, 303)) 
            fx -= 10      #   анимация       
            pygame.display.update()                         #   анимация
            time.sleep(0.1)
            display.blit(lvl1,(0,0))
            caty -= 120
            catx += 60
            display.blit(final_animation,(catx,caty))
            display.blit(text,(4,4))
            display.blit(bat,(mx, 250))
            display.blit(dontnormal,(nx, 303))
            display.blit(fire_ball,(fx, 303))
            fx -= 10
            display.blit(moster,(kx,340))
            pygame.display.update()
            jump = False
        bx -= 1
        if catx <= 100:
            graviti()
        if catx >= 185 and catx <= 557:
            graviti()
        if catx >= 101 and catx <= 285:
            graviti2()
        if catx >= 800:
            print('ты выйграл')
            f=open('lvl.txt','w')
            f.write('4')
            f.close()
            time.sleep(3)      
            exit()
        if catx == mx and 610 and jump == False:
            stopmouse = False
            health += 1
        if stopmouse == False:
            mx += 7
        if catx >= 200 and catx <= 400 and caty >= 325 and jump == False:
            caty += 3
        if caty >= 330:
            exit()
        if catx >= 557 and caty >= 240:
            x = 0
        if catx >= 659-53 and caty >= 177:
            x=0
        if catx >= 557 and catx <= 616 and caty <= 239:
            graviti2()
        if catx >= 617:
            graviti3()
        if catx >= 100 and catx < 168 and jump == False and caty >= 240:
            caty += 2
        if catx >= mx and catx - 50 <=mx:
            health += 1
            mx = 999999
        if catx == 569 and jump == False:
            exit() 
        fx -= 4
        if fx <= 0:
            fx = 550
        if fx == catx and caty >= 260:
            exit()
        if catx == 500:
            nx = 99999
        pygame.display.update()
        display.blit(lvl1,(0,0))        
        display.blit(cat,(catx,caty))    
        display.blit(text,(4,4)) 
        display.blit(moster,(kx,340))
        display.blit(bat,(mx, 250))   
        display.blit(dontnormal,(550, 303))
        display.blit(fire_ball,(fx, 303))       
        pygame.display.update()

else:
    print('пройдите 2 уровень')    