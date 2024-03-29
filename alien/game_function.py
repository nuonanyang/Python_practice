from ast import Num, alias
from asyncio import shield
import numbers
from re import T

import sys
from tkinter import E
from tkinter.tix import Tree
from zoneinfo import available_timezones

import pygame

from bullet import Bullet
from alien import Alien


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
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        

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
      
             

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(aliens,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #检查是否有子弹击中了外星人
    #若有，删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        print("space")

def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    numbers_alien_x = int(available_space_x / (2 * alien_width))
    return numbers_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1

def creat_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可以容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number)
            
        
        
def update_aliens(ai_settings,aliens):
    """检查是否有外星人位于屏幕边缘，更新外星人的位置""" 
    check_fleet_edges(ai_settings,aliens)
    aliens.update()      