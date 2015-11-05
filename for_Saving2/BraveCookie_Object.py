__author__ = 'rowell'

import random
import json
from pico2d import *


class Brave_Cookie:

    STATE_RUN, STATE_JUMP, STATE_SLIDE, STATE_DOUBLE_JUMP = 0,1,2,3
    JUMP_MAX,D_JUMP_MAX = 5,4

    def __init__(self):
       #CookieInfo = '                                                                  \
       #    {                                                                        \
       #        "x":250, "y":190,                                                    \
       #        "Once": 30, "Twice" : 40                                             \
       #    }                                                                        \
       #'

        Cookie_Info_File = open('Cookie_Info_Saved.txt','r')
        Cookie_Info = json.load(Cookie_Info_File)
        Cookie_Info_File.close()

        self.image = load_image('Brave_Cookie_Run_Jump_Slide.png')      #이미지 로드
        self.const_x, self.const_y = Cookie_Info['x'], Cookie_Info['y']
        self.x , self.y = self.const_x, self.const_y      #그려줄 좌표 초기화
        self.frame = 0      #프레임 값.
        self.Control_motion = self.STATE_RUN

        self.Change_Y = 0
        self.Chang_Y_D = 0
        self.up = True
        self.Jumping = 0
        self.Jump_Height_Once, self.Jump_Height_Twice = Cookie_Info['Once'],Cookie_Info['Twice']

    def Save(self):
        Information = []

        for name in self.Cookie_Info:
            cookie = Brave_Cookie()
            cookie.x = self.Cookie_Info['x']
            cookie.y = self.Cookie_Info['y']
            cookie.Jump_Height_Once = self.Cookie_Info['Once']
            cookie.Jump_Height_Twice =self.Cookie_Info['Twice']
            Information.append(cookie)

        return Information

    def Frame(self):
        if self.Control_motion == self.STATE_RUN :
            self.frame = (self.frame + 1 ) % 3
        elif self.Control_motion == self.STATE_JUMP: #1단 점프일 때
            self.frame = 0
        elif self.Control_motion == self.STATE_DOUBLE_JUMP :
            if self.up == True:
                self.frame = (self.frame + 1) % 4
            else :
                self.frame = 5
        elif self.Control_motion == self.STATE_SLIDE :
            self.frame = (self.frame + 1 ) % 2

    def Running(self):
        self.Control_motion = self.STATE_RUN
    def Jump(self):
        self.Control_motion = self.STATE_JUMP
    def Slide(self):
        self.Control_motion = self.STATE_SLIDE
    def Jump_Double(self):
        self.Control_motion = self.STATE_DOUBLE_JUMP

    def Jump_Change_Ysize(self) :
        #점프 중으로 바뀌었을 때.
        if self.Control_motion == self.STATE_JUMP :
            if self.Change_Y < self.JUMP_MAX :
                if self.up == True :
                    self.Change_Y += 1
                    self.y += self.Jump_Height_Once
                elif self.up == False:
                    self.Change_Y -= 1
                    self.y -= self.Jump_Height_Once
                    if self.Change_Y == 0 :
                        self.y = self.const_y
                        self.Control_motion = self.STATE_RUN
                        self.Jumping = 0
                        self.up = True
            elif self.Change_Y == self.JUMP_MAX :
                    self.up = False
                    self.Change_Y -= 1
                    self.y -= self.Jump_Height_Once
        if self.Control_motion == self.STATE_DOUBLE_JUMP :   #더블점프 중으로 바뀌었을 때.
            if self.up == True :    #위로 올라가는 중이었을때만.
                if self.Chang_Y_D < self.D_JUMP_MAX :
                    self.Chang_Y_D +=1
                    self.y += self.Jump_Height_Twice
                if self.Chang_Y_D == self.D_JUMP_MAX :    #아래로 꺼졍
                    self.Chang_Y_D -=1
                    self.y -= self.Jump_Height_Twice
                    self.up = False
            if self.up == False :   #아래로 내려가는 중
                if self.Chang_Y_D != 0 :
                    if self.Chang_Y_D > 0 :
                        self.Chang_Y_D -=1
                        self.y -= self.Jump_Height_Twice
                if self.Chang_Y_D == 0 :
                    if self.Change_Y > 0 :
                        self.Change_Y -= 1
                        self.y -= self.Jump_Height_Twice
                if self.Chang_Y_D == 0 and self.Change_Y == 0 :
                    self.y = self.const_y
                    self.Control_motion = self.STATE_RUN
                    self.frame = 0
                    self.Jumping = 0
                    self.up = True

    def draw(self):
        if self.Control_motion == self.STATE_RUN:
            self.image.clip_draw(self.frame * 120, 382-135 ,120 ,135 , self.x , self.y)
        elif self.Control_motion == self.STATE_JUMP:
            self.image.clip_draw(0, 382-135-165 ,140 ,165 , self.x , self.y)
        elif self.Control_motion == self.STATE_DOUBLE_JUMP:
            self.image.clip_draw(self.frame * 140, 382-135-165 ,140 ,165 , self.x , self.y)
        elif self.Control_motion == self.STATE_SLIDE :
            self.image.clip_draw(self.frame * 170, 382-135-165-80 ,170 ,80 , self.x , self.y-40)

    def ReDifine_Frame(self):
         self.frame = 0

    def PlusJumping(self):
        self.Jumping += 1