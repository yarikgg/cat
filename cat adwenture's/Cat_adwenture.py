# -*- coding: utf-8 -*-
import pygame
import time


w,h = 800,402
display = pygame.display.set_mode((w,h))
pygame.display.set_caption('Cat adwenture')

cat = pygame.image.load('cat.png')
cat_animation1 = pygame.image.load('cat_animation1.png')
cat_animation2 = pygame.image.load('cat_animation2.png')
final_animation = pygame.image.load('cat_animation_final.png')
lvl1 = pygame.image.load('lvl1.png')
mouse = pygame.image.load('mouse.png')
menu = pygame.image.load('menu.png')

x = 0
catx = 30
caty = 290

mx = 600

stopmouse = True

i = 2

health = 3

speed_fall=2

def graviti():
    global caty
    global speed_fall
    if caty < 290:
        jump = False
        caty += speed_fall
        if caty >= 290:
            caty = 290 
            speed_fall = 2

def graviti2():
    global caty
    global speed_fall
    graviti = False
    if caty < 230:
        jump = False
        caty += speed_fall
        if caty >= 230:
            caty = 230 
            speed_fall = 2


clock = pygame.time.Clock()

FPS = 60

game = False

jump = False

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if game == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x = 1
                if event.key == pygame.K_LEFT:
                    x = -1
                if event.key == pygame.K_SPACE:
                    if catx <= 336:
                        if caty == 290:
                            jump = True
                    elif catx >= 336 and caty == 230:
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
                if pygame.mouse.get_pos() >= (308,111):
                    if pygame.mouse.get_pos() <= (495,160):
                        game = True

    if game == True:
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
            import lvl2.py
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
    

    elif game == False:
        display.blit(menu,(0,0))
        pygame.display.update()