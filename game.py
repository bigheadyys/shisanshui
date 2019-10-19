# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *
import HHH as hh
import time
import json

class node:
    flower=0 #1234
    num=0  # 234567891011121314, A14
    def __init__(self,f,n):
        self.flower=f
        self.num=n

poker_1,poker_2,poker_3=[],[],[]    # 扑克牌分堆
for i in range(0,20):
    poker_1.append(node(0,0))
    poker_2.append(node(0, 0))
    poker_3.append(node(0, 0))

    global poker_front_1, poker_front_2, poker_front_3
    global poker_mid_1, poker_mid_2, poker_mid_3, poker_mid_4, poker_mid_5
    global poker_back_1, poker_back_2, poker_back_3, poker_back_4, poker_back_5

    poker_front_1,poker_front_2,poker_front_3 = pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png')
    poker_mid_1,poker_mid_2,poker_mid_3,poker_mid_4,poker_mid_5 = pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png')
    poker_back_1,poker_back_2,poker_back_3,poker_back_4,poker_back_5 = pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png'),pygame.image.load('素材/扑克/back.png')
    user_id = []

class TextBox:
    def __init__(self, w, h, x, y, surface, font=None, callback=None):
        """
        :param w:文本框宽度
        :param h:文本框高度
        :param x:文本框坐标
        :param y:文本框坐标
        :param font:文本框中使用的字体
        :param callback:在文本框按下回车键之后的回调函数
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # 文本框内容
        self.callback = callback
        # 创建
        self.__surface = surface
        if font is None:
            self.font = pygame.font.Font(None, 50)  # 使用pygame自带字体
        else:
            self.font = font

    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (191, 191, 191))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x +10 , self.y + (self.height - text_surf.get_height())),
                       (0, 0, self.width, self.height))

    def key_down(self, event):
        unicode = event.unicode
        key = event.key

        # 退位键
        if key == 8:
            self.text = self.text[:-1]
            return

        # 切换大小写键
        if key == 301:
            return

        # 回车键
        if key == 13:
            if self.callback is not None:
                self.callback()
            return

        if unicode != "":
            char = unicode
        else:
            char = chr(key)

        self.text += char


def callback():
    print("回车测试")


# def main():
#     # 英文文本框demo
#     pygame.init()
#     winSur = pygame.display.set_mode((640, 480))
#     # 创建文本框
#     text_box = TextBox(200, 30, 200, 200, callback = callback)
# #
# #     # 游戏主循环
# #     while True:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 exit()
# #             elif event.type == pygame.KEYDOWN:
# #                 text_box.key_down(event)
# #         pygame.time.delay(33)
# #         winSur.fill((0, 50, 0))
# #         text_box.draw(winSur)
# #         pygame.display.flip()


# class poker():
    # def __init__(self):

class Game_status():
    def __init__(self,page = 1):
        self.page = page

# def poker_image(poker,poker_image):
#     if poker.flower == '&':
#         if poker.num == '1':
#             poker_image = pygame.image.load('素材/扑克/0.png').cnvert_alpha()
#         if poker.num == '2':
#             poker_image = pygame.image.load('素材/扑克/1.png').cnvert_alpha()
#         if poker.num == '3':
#             poker_image = pygame.image.load('素材/扑克/2.png').cnvert_alpha()
#         if poker.num == '4':
#             poker_image = pygame.image.load('素材/扑克/3.png').cnvert_alpha()
#         if poker.num == '5':
#             poker_image = pygame.image.load('素材/扑克/4.png').cnvert_alpha()
#         if poker.num == '6':
#             poker_image = pygame.image.load('素材/扑克/5.png').cnvert_alpha()
#         if poker.num == '7':
#             poker_image = pygame.image.load('素材/扑克/6.png').cnvert_alpha()
#         if poker.num == '8':
#             poker_image = pygame.image.load('素材/扑克/7.png').cnvert_alpha()
#         if poker.num == '9':
#             poker_image = pygame.image.load('素材/扑克/8.png').cnvert_alpha()
#         if poker.num == '10':
#             poker_image = pygame.image.load('素材/扑克/9.png').cnvert_alpha()
#         if poker.num == 'J':
#             poker_image = pygame.image.load('素材/扑克/10.png').cnvert_alpha()
#         if poker.num == 'Q':
#             poker_image = pygame.image.load('素材/扑克/11.png').cnvert_alpha()
#         if poker.num == 'K':
#             poker_image = pygame.image.load('素材/扑克/12.png').cnvert_alpha()
#     if poker.flower == '$':
#         if poker.num == '1':
#             poker_image = pygame.image.load('素材/扑克/13.png').cnvert_alpha()
#         if poker.num == '2':
#             poker_image = pygame.image.load('素材/扑克/14.png').cnvert_alpha()
#         if poker.num == '3':
#             poker_image = pygame.image.load('素材/扑克/15.png').cnvert_alpha()
#         if poker.num == '4':
#             poker_image = pygame.image.load('素材/扑克/16.png').cnvert_alpha()
#         if poker.num == '5':
#             poker_image = pygame.image.load('素材/扑克/17.png').cnvert_alpha()
#         if poker.num == '6':
#             poker_image = pygame.image.load('素材/扑克/18.png').cnvert_alpha()
#         if poker.num == '7':
#             poker_image = pygame.image.load('素材/扑克/19.png').cnvert_alpha()
#         if poker.num == '8':
#             poker_image = pygame.image.load('素材/扑克/20.png').cnvert_alpha()
#         if poker.num == '9':
#             poker_image = pygame.image.load('素材/扑克/21.png').cnvert_alpha()
#         if poker.num == '10':
#             poker_image = pygame.image.load('素材/扑克/22.png').cnvert_alpha()
#         if poker.num == 'J':
#             poker_image = pygame.image.load('素材/扑克/23.png').cnvert_alpha()
#         if poker.num == 'Q':
#             poker_image = pygame.image.load('素材/扑克/24.png').cnvert_alpha()
#         if poker.num == 'K':
#             poker_image = pygame.image.load('素材/扑克/25.png').cnvert_alpha()
#     if poker.flower == '#':
#         if poker.num == '1':
#             poker_image = pygame.image.load('素材/扑克/26.png').cnvert_alpha()
#         if poker.num == '2':
#             poker_image = pygame.image.load('素材/扑克/27.png').cnvert_alpha()
#         if poker.num == '3':
#             poker_image = pygame.image.load('素材/扑克/28.png').cnvert_alpha()
#         if poker.num == '4':
#             poker_image = pygame.image.load('素材/扑克/29.png').cnvert_alpha()
#         if poker.num == '5':
#             poker_image = pygame.image.load('素材/扑克/30.png').cnvert_alpha()
#         if poker.num == '6':
#             poker_image = pygame.image.load('素材/扑克/31.png').cnvert_alpha()
#         if poker.num == '7':
#             poker_image = pygame.image.load('素材/扑克/32.png').cnvert_alpha()
#         if poker.num == '8':
#             poker_image = pygame.image.load('素材/扑克/33.png').cnvert_alpha()
#         if poker.num == '9':
#             poker_image = pygame.image.load('素材/扑克/34.png').cnvert_alpha()
#         if poker.num == '10':
#             poker_image = pygame.image.load('素材/扑克/35.png').cnvert_alpha()
#         if poker.num == 'J':
#             poker_image = pygame.image.load('素材/扑克/36.png').cnvert_alpha()
#         if poker.num == 'Q':
#             poker_image = pygame.image.load('素材/扑克/37.png').cnvert_alpha()
#         if poker.num == 'K':
#             poker_image = pygame.image.load('素材/扑克/38.png').cnvert_alpha()
#     if poker.flower == '*':
#         if poker.num == '1':
#             poker_image = pygame.image.load('素材/扑克/39.png').cnvert_alpha()
#         if poker.num == '2':
#             poker_image = pygame.image.load('素材/扑克/40.png').cnvert_alpha()
#         if poker.num == '3':
#             poker_image = pygame.image.load('素材/扑克/41.png').cnvert_alpha()
#         if poker.num == '4':
#             poker_image = pygame.image.load('素材/扑克/42.png').cnvert_alpha()
#         if poker.num == '5':
#             poker_image = pygame.image.load('素材/扑克/43.png').cnvert_alpha()
#         if poker.num == '6':
#             poker_image = pygame.image.load('素材/扑克/44.png').cnvert_alpha()
#         if poker.num == '7':
#             poker_image = pygame.image.load('素材/扑克/45.png').cnvert_alpha()
#         if poker.num == '8':
#             poker_image = pygame.image.load('素材/扑克/46.png').cnvert_alpha()
#         if poker.num == '9':
#             poker_image = pygame.image.load('素材/扑克/47.png').cnvert_alpha()
#         if poker.num == '10':
#             poker_image = pygame.image.load('素材/扑克/48.png').cnvert_alpha()
#         if poker.num == 'J':
#             poker_image = pygame.image.load('素材/扑克/49.png').cnvert_alpha()
#         if poker.num == 'Q':
#             poker_image = pygame.image.load('素材/扑克/50.png').cnvert_alpha()
#         if poker.num == 'K':
#             poker_image = pygame.image.load('素材/扑克/51.png').cnvert_alpha()

def change(flower,num):
    x=(flower-1)*13+(num-2)
    str0='素材/扑克/'
    str0+=str(x)+'.png'
    return str0


def choosecard():
    global poker_front_1, poker_front_2, poker_front_3
    global poker_mid_1, poker_mid_2, poker_mid_3, poker_mid_4, poker_mid_5
    global poker_back_1, poker_back_2, poker_back_3, poker_back_4, poker_back_5

    for i in range(1,3+1):
        poker_1[i]= hh.end_3[i]
    for i in range(1,5+1):
        poker_2[i]= hh.end_2[i]
    for i in range(1, 5 + 1):
        poker_3[i] = hh.end_1[i]

    poker_front_1 = pygame.image.load(change(poker_1[1].flower,poker_1[1].num))
    poker_front_2 = pygame.image.load(change(poker_1[2].flower,poker_1[2].num))
    poker_front_3 = pygame.image.load(change(poker_1[3].flower,poker_1[3].num))

    poker_mid_1 = pygame.image.load(change(poker_2[1].flower,poker_2[1].num))
    poker_mid_2 = pygame.image.load(change(poker_2[2].flower,poker_2[2].num))
    poker_mid_3 = pygame.image.load(change(poker_2[3].flower,poker_2[3].num))
    poker_mid_4 =pygame.image.load(change(poker_2[4].flower,poker_2[4].num))
    poker_mid_5 = pygame.image.load(change(poker_2[5].flower,poker_2[5].num))

    poker_back_1 = pygame.image.load(change(poker_3[1].flower,poker_3[1].num))
    poker_back_2 = pygame.image.load(change(poker_3[2].flower,poker_3[2].num))
    poker_back_3 = pygame.image.load(change(poker_3[3].flower,poker_3[3].num))
    poker_back_4 = pygame.image.load(change(poker_3[4].flower,poker_3[4].num))
    poker_back_5 = pygame.image.load(change(poker_3[5].flower,poker_3[5].num))

def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("福建十三水")  # 窗口名字
    window_icon = pygame.image.load('素材/窗口图标.png').convert_alpha()
    pygame.display.set_icon(window_icon)
    status = Game_status()  # 游戏状态
    # 创建文本框
    text_box1 = TextBox(280, 55, 763, 233,pygame.image.load('素材/登录输入框.png'), callback = callback)
    text_box2 = TextBox(280, 55, 763, 338,pygame.image.load('素材/登录输入框.png'), callback = callback)
    text_box2_fake = TextBox(280, 55, 763, 338,pygame.image.load('素材/登录输入框.png'), callback = callback)
    text_box1_status = False
    text_box2_status = False



    login_background = pygame.image.load('素材/登录背景.png') #登录界面
    login_button = pygame.image.load('素材/登录按钮.png')
    zhuce_button = pygame.image.load('素材/注册按钮.png')

    menu_background = pygame.image.load('素材/主菜单背景.png')    #主菜单界面
    menu_button_jryx = pygame.image.load('素材/主菜单进入游戏按钮.png').convert_alpha()
    menu_button_lsyx = pygame.image.load('素材/主菜单历史游戏按钮.png').convert_alpha()
    menu_button_phb = pygame.image.load('素材/主菜单排行榜按钮.png').convert_alpha()
    menu_button_exit = pygame.image.load('素材/主菜单退出登录按钮.png').convert_alpha()

    jryx_background = pygame.image.load('素材/进入游戏背景.png')
    jryx_button_return = pygame.image.load('素材/进入游戏返回主菜单按钮.png')
    jryx_button_start = pygame.image.load('素材/进入游戏开始游戏按钮.png')

    lsyx_background = pygame.image.load('素材/历史游戏背景.png')
    phb_background = pygame.image.load('素材/排行榜背景.png')

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if status.page == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 765 < mouse_x < 765 + 391 and 447 < mouse_y < 447 + 69:
                        message = hh.login("w111700632", "wuzhihao.")
                        user_id = message["data"]["user_id"]
                        print(user_id)
                        status.page = 2
                    # if 765 < mouse_x < 765 + 391 and 543 < mouse_y < 543 + 74:
                    #     hh.registered(text_box1.text, text_box2.text)
                    if 763 < mouse_x < 763+393 and 233 < mouse_y < 233+74 :
                        text_box1_status = True
                    else :
                        text_box1_status = False
                    if 763 < mouse_x < 763+393 and 338 < mouse_y < 338 + 74 :
                        text_box2_status = True
                    else :
                        text_box2_status = False
                if event.type == pygame.KEYDOWN:
                    if text_box1_status == True:
                        text_box1.key_down(event)
                        pygame.time.delay(33)
                    if text_box2_status == True:
                        text_box2.key_down(event)
                        pygame.time.delay(33)





            elif status.page == 2:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 54 < mouse_x < 54 + 328 + 10 and 186 < mouse_y < 186 + 441:
                    menu_button_jryx = pygame.image.load('素材/主菜单进入游戏按钮半透明.png').convert_alpha()
                else:
                    menu_button_jryx = pygame.image.load('素材/主菜单进入游戏按钮.png').convert_alpha()
                if 468 < mouse_x < 468 + 328 and 186 < mouse_y < 186 + 441:
                    menu_button_lsyx = pygame.image.load('素材/主菜单历史游戏按钮半透明.png').convert_alpha()
                else:
                    menu_button_lsyx = pygame.image.load('素材/主菜单历史游戏按钮.png').convert_alpha()
                if 890 < mouse_x < 890 + 328 and 186 < mouse_y < 186 + 441:
                    menu_button_phb = pygame.image.load('素材/主菜单排行榜按钮半透明.png').convert_alpha()
                else:
                    menu_button_phb = pygame.image.load('素材/主菜单排行榜按钮.png').convert_alpha()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 939 < mouse_x < 939 + 267 + 7 and 28 + 7 < mouse_y < 28 + 7 + 64:
                        status.page = 1
                    if 54 < mouse_x < 54 + 328 and 186 < mouse_y < 186 + 441:
                        status.page = 3
                        # hh.read_opengame()  # 开启牌局，读入
                        # hh.dfs_1(1, 1)#解决问题，深搜
                        # hh.submit_ans=hh.printf_ans()
                        # # print(submit_ans)
                        # hh.submitgame(hh.submit_ans)#提交牌局

                    if 468 < mouse_x < 468 + 328 and 186 < mouse_y < 186 + 441:
                        status.page = 4
                        message1 = hh.history(3, 1)
                        data = message1["data"]
                        data2 = json.loads(data)
                        print(data2)
                    if 890 < mouse_x < 890 + 328 and 186 < mouse_y < 186 + 441:
                        status.page = 5

            elif status.page == 3:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 76 < mouse_x < 76 + 267 + 7 and 18 < mouse_y < 18 + 64 + 5:
                        print('ininin')
                        timestart = time.clock()
                        hh.init_start()
                        hh.read_opengame()
                        hh.dfs_1(1, 1)  # 解决问题，深搜
                        hh.submit_ans = hh.printf_ans()
                        hh.submitgame(hh.submit_ans)  # 提交牌局
                        timeend = time.clock()
                        print("used time:" + str(timeend - timestart))
                        choosecard()


                    if 927 < mouse_x < 927 + 267 + 7 and 18 < mouse_y < 18 + 64 + 5:
                        status.page = 2

            elif status.page == 4:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 0 < mouse_x < 83 and 0 < mouse_y < 61:
                        status.page = 2



            elif status.page == 5:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 0 < mouse_x < 83 and 0 < mouse_y < 61:
                        status.page = 2
                    name1 = "hanhan"
                    name2 = "hanhan"
                    name3 = "hanhan"
                    score1 = str(999)
                    score2 = str(999)
                    score3 = str(999)
                    id1 = str(999)
                    id2 = str(999)
                    id3 = str(999)


        # text_1 = ''.join(message_yhm)
        # text_2 = ''.join([len(message_mm)*'·'])

        if status.page == 1:  # 登录界面刷新内容
            screen.blit(login_background, (0, 0))
            screen.blit(login_button, (765, 447))
            screen.blit(zhuce_button, (765, 543))
            text_box1.draw(screen)
            text_box2_fake.text =''.join(['·'*len(text_box2.text)])
            text_box2_fake.draw(screen)
            # if len(message_yhm) == 0:
            #     screen.blit(pygame.font.SysFont("arial", 33).render('Enter your username', True, (191, 191, 191)),
            #                 (361, 136))
            # else:
            #     screen.blit(pygame.font.SysFont('arial', 33).render(text_1, True, (127, 127, 127)), (361, 136))
            # if len(message_mm) == 0:
            #     screen.blit(pygame.font.SysFont("arial", 33).render('Enter your password', True, (191, 191, 191)),
            #                 (361, 198))
            # else:
            #     screen.blit(pygame.font.SysFont('arial', 45).render(text_2, True, (127, 127, 127)), (361, 198))

        if status.page == 2:  # 主菜单界面刷新内容
            screen.blit(menu_background, (0, 0))
            # screen.blit(pygame.font.SysFont("微软雅黑", 20).render(user_id, True, (255, 255, 255)), (135, 16))
            screen.blit(menu_background, (0, 0))
            screen.blit(menu_button_jryx, (54, 186))
            screen.blit(menu_button_lsyx, (468, 186))
            screen.blit(menu_button_phb, (890, 186))
            screen.blit(menu_button_exit, (940, 30))

        if status.page == 3:  # 游戏界面刷新内容


            screen.blit(jryx_background, (0, 0))
            screen.blit(jryx_button_return, (927, 18))
            screen.blit(jryx_button_start, (76, 18))
            # poker 前墩
            screen.blit(poker_front_1, (50+320, 132))
            screen.blit(poker_front_2, (50+420, 132))
            screen.blit(poker_front_3, (50+520, 132))
            # poker 中墩
            screen.blit(poker_mid_1, (50+320, 280))
            screen.blit(poker_mid_2, (50+420, 280))
            screen.blit(poker_mid_3, (50+520, 280))
            screen.blit(poker_mid_4, (50+620, 280))
            screen.blit(poker_mid_5, (50+720, 280))
            # poker 后墩
            screen.blit(poker_back_1, (50+320, 430))
            screen.blit(poker_back_2, (50+420, 430))
            screen.blit(poker_back_3, (50+520, 430))
            screen.blit(poker_back_4, (50+620, 430))
            screen.blit(poker_back_5, (50+720, 430))

        if status.page == 4:  # 历史游戏界面刷新内容
            screen.blit(lsyx_background, (0, 0))

        if status.page == 5:  # 历史游戏界面刷新内容
            screen.blit(phb_background, (0, 0))

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()

# mouse_x, mouse_y = pygame.mouse.get_pos()
# if 361 < mouse_x < 361 + 259 and 136 < mouse_y < 136 + 45:
#     # print('mouse in the box')
#     if event.type == KEYDOWN:
#         key_num = event.key
#         if key_num == 49:
#             message_yhm.append('1')  # get the value of keyboard
#         elif key_num == 50:
#             message_yhm.append('2')  # get the value of keyboard
#         elif key_num == 51:
#             message_yhm.append('3')  # get the value of keyboard
#         elif key_num == 52:
#             message_yhm.append('4')  # get the value of keyboard
#         elif key_num == 53:
#             message_yhm.append('5')  # get the value of keyboard
#         elif key_num == 54:
#             message_yhm.append('6')  # get the value of keyboard
#         elif key_num == 55:
#             message_yhm.append('7')  # get the value of keyboard
#         elif key_num == 56:
#             message_yhm.append('8')  # get the value of keyboard
#         elif key_num == 57:
#             message_yhm.append('9')  # get the value of keyboard
#         elif key_num == 48:
#             message_yhm.append('0')  # get the value of keyboard
#         elif key_num == 97:
#             message_yhm.append('A')  # get the value of keyboard
#         elif key_num == 8 and len(message_yhm) is not 0:
#             message_yhm.pop()  # delete the last value
#
# elif 361 < mouse_x < 361 + 259 and 198 < mouse_y < 198 + 45:
#     # print('mouse in the box2')
#     if event.type == KEYDOWN:
#         key_num = event.key
#         if key_num == 49:
#             message_mm.append('1')  # get the value of keyboard
#         elif key_num == 50:
#             message_mm.append('2')  # get the value of keyboard
#         elif key_num == 51:
#             message_mm.append('3')  # get the value of keyboard
#         elif key_num == 52:
#             message_mm.append('4')  # get the value of keyboard
#         elif key_num == 53:
#             message_mm.append('5')  # get the value of keyboard
#         elif key_num == 54:
#             message_mm.append('6')  # get the value of keyboard
#         elif key_num == 55:
#             message_mm.append('7')  # get the value of keyboard
#         elif key_num == 56:
#             message_mm.append('8')  # get the value of keyboard
#         elif key_num == 57:
#             message_mm.append('9')  # get the value of keyboard
#         elif key_num == 48:
#             message_mm.append('0')  # get the value of keyboard
#         elif key_num == 97:
#             message_mm.append('A')  # get the value of keyboard
#         elif key_num == 8 and len(message_mm) is not 0:
#             message_mm.pop()  # delete the last value
