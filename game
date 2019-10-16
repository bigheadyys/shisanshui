# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *
import HHH as hh

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
        # 如果font为None,那么效果可能不太好，建议传入font，更好调节
        if font is None:
            self.font = pygame.font.Font(None, 32)  # 使用pygame自带字体
        else:
            self.font = font

    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
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


def main():
    # 英文文本框demo
    pygame.init()
    winSur = pygame.display.set_mode((640, 480))
    # 创建文本框
    text_box = TextBox(200, 30, 200, 200, callback = callback)
#
#     # 游戏主循环
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit()
#             elif event.type == pygame.KEYDOWN:
#                 text_box.key_down(event)
#         pygame.time.delay(33)
#         winSur.fill((0, 50, 0))
#         text_box.draw(winSur)
#         pygame.display.flip()


# class poker():
    # def __init__(self):

class Game_status():
    def __init__(self,page = 1):
        self.page = page

def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("福建十三水")  # 窗口名字
    window_icon = pygame.image.load('素材/窗口图标.png').convert_alpha()
    pygame.display.set_icon(window_icon)
    status = Game_status()  # 游戏状态
    # 创建文本框
    text_box1 = TextBox(200, 30, 763, 233,pygame.image.load('素材/登录输入框.png'), callback = callback)
    text_box2 = TextBox(200, 30, 763, 338,pygame.image.load('素材/登录输入框.png'), callback = callback)
    message_yhm = []
    message_mm = []
    user_id = []#输入框

    login_background = pygame.image.load('素材/登录背景.png') #登录界面
    login_button = pygame.image.load('素材/登录按钮.png')
    zhuce_button = pygame.image.load('素材/注册按钮.png')
    menu_background = pygame.image.load('素材/主菜单背景.png')    #主菜单界面
    menu_button_jryx = pygame.image.load('素材/主菜单进入游戏按钮.png').convert_alpha()
    menu_button_cjfj = pygame.image.load('素材/主菜单创建房间按钮.png').convert_alpha()
    menu_button_lsyx = pygame.image.load('素材/主菜单历史游戏按钮.png').convert_alpha()
    menu_button_phb = pygame.image.load('素材/主菜单排行榜按钮.png').convert_alpha()
    menu_button_exit = pygame.image.load('素材/主菜单退出登录按钮.png').convert_alpha()
    jryx_background = pygame.image.load('素材/进入游戏背景.png')

    lsyx_background = pygame.image.load('素材/历史游戏背景.png')
    phb_background = pygame.image.load('素材/排行榜背景.png')

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if status.page == 1:
                # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #     mouse_x, mouse_y = pygame.mouse.get_pos()
                #     if 361 < mouse_x < 361 + 125 and 264 < mouse_y < 264 + 37:
                #         text1 = ''.join(message_yhm)
                #         text2 = ''.join(message_yhm)
                #         login_js = hh.login(text1, str(text2))
                #         print(login_js)
                #         user_id = ''.join(str(login_js["data"]["user_id"]))
                #         status.page = 2
                #     if 495 < mouse_x < 495 + 125 and 264 < mouse_y < 264 + 37:
                #         text1 = ''.join(message_yhm)
                #         text2 = ''.join(message_yhm)
                #         hh.registered(text1, text2)
                if event.type == pygame.KEYDOWN:
                        text_box1.key_down(event)
                        pygame.time.delay(33)
                        text_box1.draw(screen)


            elif status.page == 2:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if 713 < mouse_x < 713 + 125 and 9 < mouse_y < 9 + 38:
                        status.page = 1
                    if 135 < mouse_x < 135 + 165 and 109 < mouse_y < 109 + 251:
                        status.page = 3
                        # hh.read_opengame()  # 开启牌局，读入
                        # hh.dfs_1(1, 1)#解决问题，深搜
                        # hh.submit_ans=hh.printf_ans()
                        # # print(submit_ans)
                        # hh.submitgame(hh.submit_ans)#提交牌局

                    if 17 < mouse_x < 17 + 158 and 396 < mouse_y < 396 + 72:
                        status.page = 5
                    if 181 < mouse_x < 181 + 158 and 396 < mouse_y < 396 + 72:
                        status.page = 4
                # if 109 < mouse_y < 109 + 251 and 135 < mouse_x < 135 + 162:
                #     menu_button_jryx = pygame.image.load('素材/主菜单进入游戏按钮变大.png')
                # else:
                #     menu_button_jryx = pygame.image.load('素材/主菜单进入游戏按钮.png')
                if 396 < mouse_y < 396 + 72 and 17 < mouse_x < 17 + 158:
                    menu_button_lsyx = pygame.image.load('素材/主菜单历史游戏按钮半透明.png')
                else:
                    menu_button_lsyx = pygame.image.load('素材/主菜单历史游戏按钮.png')
                if 396 < mouse_y < 396 + 72 and 181 < mouse_x < 181 + 158:
                    menu_button_phb = pygame.image.load('素材/主菜单排行榜按钮半透明.png')
                else:
                    menu_button_phb = pygame.image.load('素材/主菜单排行榜按钮.png')

            elif status.page == 3:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 811 < mouse_x < 811 + 28 and 15 < mouse_y < 15 + 28:
                        status.page = 2
                    if 0 < mouse_x < 200 and 0 < mouse_y < 200:
                        print('ininin')
                        hh.read_opengame()
                        hh.dfs_1(1, 1)#解决问题，深搜
                        hh.submit_ans=hh.printf_ans()
                        # print(submit_ans)
                        hh.submitgame(hh.submit_ans)#提交牌局


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


        text_1 = ''.join(message_yhm)
        text_2 = ''.join([len(message_mm)*'·'])

        if status.page == 1:  # 登录界面刷新内容
            screen.blit(login_background, (0, 0))
            screen.blit(login_button, (765, 447))
            screen.blit(zhuce_button, (765, 543))
            text_box1.draw(screen)
            text_box2.draw(screen)
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
            screen.blit(pygame.font.SysFont("微软雅黑", 20).render(user_id, True, (255, 255, 255)), (135, 16))
            screen.blit(menu_button_jryx, (135, 109))
            screen.blit(menu_button_phb, (181, 396))
            screen.blit(menu_button_lsyx, (17, 396))
            screen.blit(menu_button_cjfj, (408, 109))
            screen.blit(menu_button_exit, (713, 9))

        if status.page == 3:  # 游戏界面刷新内容
            screen.blit(jryx_background, (0, 0))

            # # poker 前墩
            # screen.blit(poker_front_1, (20,10))
            # screen.blit(poker_front_2, (20, 70))
            # screen.blit(poker_front_3, (20, 130))
            # # poker 中墩
            # screen.blit(poker_mid_1, (120, 10))
            # screen.blit(poker_mid_2, (120, 70))
            # screen.blit(poker_mid_3, (120, 130))
            # screen.blit(poker_mid_4, (120, 190))
            # screen.blit(poker_mid_5, (120, 250))
            # # poker 后墩
            # screen.blit(poker_back_1, (220, 10))
            # screen.blit(poker_back_2, (220, 70))
            # screen.blit(poker_back_3, (220, 130))
            # screen.blit(poker_back_4, (220, 190))
            # screen.blit(poker_back_5, (220, 250))

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
