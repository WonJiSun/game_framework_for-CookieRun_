__author__ = 'rowell'

import random
import main_state
from pico2d import *


class Brave_Cookie:
    def __init__(self):
        self.image = load_image('Brave_Cookie_Run_Jump_Slide.png')      #이미지 로드
        self.x , self.y = 250, 190      #그려줄 좌표 초기화
        self.frame = 0      #프레임 값.
        self.Control_motion = 0

        self.Change_Y = 0
        self.Chang_Y_D = 0
        self.up = True
        self.Jumping = 0
    def Frame(self):
        if self.Control_motion == 0 :
            self.frame = (self.frame + 1 ) % 3
        elif self.Control_motion == 1: #1단 점프일 때
            self.frame = 0
        elif self.Control_motion == 3 :
            if self.up == True:
                self.frame = (self.frame + 1) % 4
            else :
                self.frame = 5
        elif self.Control_motion == 2 :
            self.frame = (self.frame + 1 ) % 2

    def Running(self):
        self.Control_motion = 0
    def Jump(self):
        self.Control_motion = 1
    def Slide(self):
        self.Control_motion = 2
    def Jump_Double(self):
        self.Control_motion = 3

    def Jump_Change_Ysize(self) :

        if self.Control_motion == 1 :   #점프 중으로 바뀌었을 때.
            if self.Change_Y < 5 :
                if self.up == True :
                    self.Change_Y += 1
                    self.y += 30
                elif self.up == False:
                    self.Change_Y -= 1
                    self.y -= 30
                    if self.Change_Y == 0 :
                        self.y = 150
                        self.Control_motion = 0
                        self.Jumping = 0
                        self.up = True
            elif self.Change_Y == 5 :
                    self.up = False
                    self.Change_Y -= 1
                    self.y -= 30
        if self.Control_motion == 3 :   #더블점프 중으로 바뀌었을 때.
            if self.up == True :    #위로 올라가는 중이었을때만.
                if self.Chang_Y_D < 4 :
                    self.Chang_Y_D +=1
                    self.y += 30
                if self.Chang_Y_D == 4 :    #아래로 꺼졍
                    self.Chang_Y_D -=1
                    self.y -= 30
                    self.up = False
            if self.up == False :   #아래로 내려가는 중
                if self.Chang_Y_D != 0 :
                    if self.Chang_Y_D > 0 :
                        self.Chang_Y_D -=1
                        self.y -= 30
                if self.Chang_Y_D == 0 :
                    if self.Change_Y > 0 :
                        self.Change_Y -= 1
                        self.y -= 30
                if self.Chang_Y_D == 0 and self.Change_Y == 0 :
                    self.y = 150
                    self.Control_motion = 0
                    self.frame = 0
                    self.Jumping = 0
                    self.up = True

    def draw(self):
        if self.Control_motion == 0:
            self.image.clip_draw(self.frame * 120, 382-135 ,120 ,135 , self.x , self.y)
        elif self.Control_motion == 1:
            self.image.clip_draw(0, 382-135-165 ,140 ,165 , self.x , self.y)
        elif self.Control_motion == 3:
            self.image.clip_draw(self.frame * 140, 382-135-165 ,140 ,165 , self.x , self.y)
        elif self.Control_motion == 2 :
            self.image.clip_draw(self.frame * 170, 382-135-165-80 ,170 ,80 , self.x , self.y-40)

    def ReDifine_Frame(self):
         self.frame = 0

    def PlusJumping(self):
        self.Jumping +=1