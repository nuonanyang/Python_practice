from asyncio import shield
from re import T

import sys
from tkinter import E
from tkinter.tix import Tree

import pygame

from bullet import Bullet


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        #向右移动飞船
        # ship.rect.centerx +=1
        ship.moving_right = True
        print("right_down")
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        print("lef_down")

    elif event.key == pygame.K_SPACE:
        #创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings,screen.ship)
        bullets.add(new_bullet)
        print("space")

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        print("right_up")
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        print("left_up")



def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit("exit")
        
        elif event.type == pygame.KEYDOWN:
           check_keydown_events(event,ai_settings,screen,ship,bullets)
                  
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            

        
            
             

def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()


    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()