from email.headerregistry import Group
from pkgutil import ImpImporter
# import sys
from turtle import Screen

import pygame

from settings import Settings
from ship import Ship
# from alien import Alien
import game_function as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
 
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship =Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建一个外星人
    # alien = Alien(ai_settings,screen)

    aliens =  Group()

    #创建外星人群
    gf.creat_fleet(ai_settings,screen,ship,aliens)
 

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        
        gf.check_events(ai_settings,screen,ship,bullets)

        ship.update()

        gf.update_bullets(aliens,bullets)
        
        gf.update_aliens(ai_settings,aliens)
      
               
        #每次循环时都重绘屏幕

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
