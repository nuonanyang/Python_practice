# coding=utf-8

#     event = pygame.event.wait()
#     if event.type == pygame.QUIT:
#         sys.exit()

#     # def check_events():
#         """响应按键和鼠标事件"""
#         # for event in pygame.event.get():
            

#         #     if event.type == pygame.QUIT:
#         #         sys.exit()
            
            
            
#     elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_RIGHT:
#             print("down")

#     elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_RIGHT:
#             print("up")


import pygame
from random import randint

# 初始化程序
pygame.init()
screen = pygame.display.set_mode((450,400))
pygame.display.set_caption("c语言中文网")
# 更新显示
pygame.display.flip()

while True:
    #等待事件发生
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit("成功退出")

    if event.type == pygame.MOUSEBUTTONDOWN:
        # pos 获取鼠标当前位置
        print('鼠标按下',event.pos)
        mx,my = event.pos
        # 调用 pygame.draw 模块画圆
        pygame.draw.circle(screen,(255,255,0),(mx,my),50)
        # 处理完，更新显示
        pygame.display.update()
    if event.type == pygame.MOUSEBUTTONUP:
        print('鼠标弹起')
        pass

    if event.type == pygame.MOUSEMOTION:
        print('鼠标移动')
        mx, my = event.pos
        # 随机生成 RGB 颜色值
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        pygame.draw.circle(screen, (r,g,b,),(mx, my), 50)
        # 处理完，更新显示
        pygame.display.update()

             
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            print("down")

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            print("up")