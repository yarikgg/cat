f=open('lvl.txt','r')
chek = f.read()
f.close()

if chek >= '2':
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
    lvl1 = pygame.image.load('lvl2.png')
    mouse = pygame.image.load('mouse.png')

    x = 0
    catx = 30
    caty = 325

    mx = 600

    bx = 250

    stopmouse = True

    kx = 250

    i = 2

    health = 3

    def graviti():
        global caty
        global catx
        if caty <= 325:
            caty += 2
            if caty >= 325:
                caty = 325

    def graviti2():
        global caty
        global catx
        graviti = False
        if caty <= 267:
            caty += 2
            if caty >= 267:
                caty = 267  

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
        if caty < 324 and catx >= 285 and catx <= 380:
            jump=False
        if jump == True:
            display.blit(lvl1,(0,0))                        #   анимация
            display.blit(cat_animation1,(catx,caty))
            display.blit(text,(4,4))  
            display.blit(moster,(kx,325))
            display.blit(mouse,(mx, 355))      #   анимация
            pygame.display.update()                         #   анимация   
            time.sleep(0.3)                                 #   анимация
            display.blit(lvl1,(0,0))                        #   анимация
            display.blit(cat_animation2,(catx,caty))
            display.blit(text,(4,4))
            display.blit(moster,(kx,325))
            display.blit(mouse,(mx, 355))        #   анимация       
            pygame.display.update()                         #   анимация
            time.sleep(0.3)
            display.blit(lvl1,(0,0))
            caty -= 120
            catx += 60
            display.blit(final_animation,(catx,caty))
            display.blit(text,(4,4))
            display.blit(mouse,(mx, 355))
            display.blit(moster,(kx,325))
            pygame.display.update()
            jump = False
        bx -= 1
        if catx <= 186:
            graviti()
        if catx >= 328:
            graviti()
        if catx >= 197 and catx <= 328:
            graviti2()
        if catx >= 800:
            print('ты выйграл')
            f=open('lvl.txt','w')
            f.write('3')
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
        pygame.display.update()
        display.blit(lvl1,(0,0))        
        display.blit(cat,(catx,caty))    
        display.blit(text,(4,4)) 
        display.blit(moster,(kx,325))
        display.blit(mouse,(mx, 355))          
        pygame.display.update()

else:
    print('пройдите 1 уровень!')
    