import pygame
import time


w,h = 800,402
display = pygame.display.set_mode((w,h))

cat = pygame.image.load('cat.png')
cat_animation1 = pygame.image.load('cat_animation1.png')
cat_animation2 = pygame.image.load('cat_animation2.png')
final_animation = pygame.image.load('cat_animation_final.png')
lvl1 = pygame.image.load('lvl1.png')
mouse = pygame.image.load('mouse.png')

x = 0
catx = 30
caty = 290

mx = 600

stopmouse = True

i = 2

health = 3

def graviti():
    global caty
    global catx
    if caty < 290:
        caty += 2
        if caty >= 290:
            caty = 290 

def graviti2():
    global caty
    global catx
    graviti = False
    if caty < 230:
        caty += 2
        if caty >= 230:
            caty = 230 

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

    #f = pygame.font.SysFont('arial', 48)
    #text = f.render('здоровье='+str(health), True,
    #    (0, 180, 0))
    clock.tick(FPS)
    if x == 1:
        catx += 2
    if x == -1:
        catx -= 2
    if jump == True:
        display.blit(lvl1,(0,0))                        #   анимация
        display.blit(cat_animation1,(catx,caty))
        #display.blit(text,(4,4))  
        display.blit(mouse,(mx, 255))      #   анимация
        pygame.display.update()                         #   анимация   
        time.sleep(0.3)                                 #   анимация
        display.blit(lvl1,(0,0))                        #   анимация
        display.blit(cat_animation2,(catx,caty))
        #display.blit(text,(4,4))
        display.blit(mouse,(mx, 255))        #   анимация       
        pygame.display.update()                         #   анимация
        time.sleep(0.3)
        display.blit(lvl1,(0,0))
        caty -= 120
        catx += 70
        display.blit(final_animation,(catx,caty))
        #display.blit(text,(4,4))
        display.blit(mouse,(mx, 255))
        pygame.display.update()
        jump = False
    if catx <= 336:
        graviti()
    if catx >= 350 and caty >= 250:
        x = 0
    if catx >= 337:
        graviti2()
    if catx >= 800:
        print('ты выйграл')
        win = pygame.font.SysFont('serif', 48)
        wintext = win.render('You Win!', True,
                (180, 180, 0))
        display.blit(wintext,(800//2,402//2))
        time.sleep(3)      
        exit()
    if catx == 520 and 561 and jump == False:
        health -= 1
    if health == 0:
        exit()
    if catx == mx and 610 and jump == False:
        stopmouse = False
        health += 1
    if stopmouse == False:
        mx += 7
    display.blit(lvl1,(0,0))        
    display.blit(cat,(catx,caty))    
    #display.blit(text,(4,4)) 
    display.blit(mouse,(mx, 255)) 
    pygame.display.update()
    

