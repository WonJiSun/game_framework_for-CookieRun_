__author__ = 'rowell'

import random
import json
from pico2d import *


class Brave_Cookie:
    #jump speed
    PIXEL_PER_METER = (10.0 / 1.5)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)  # 20000 / 60 //300몇..
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)        # 5..
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER) # 50 / 30

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    STATE_RUN, STATE_JUMP, STATE_SLIDE, STATE_DOUBLE_JUMP = 0,1,2,3
    JUMP_MAX,D_JUMP_MAX = 50,50

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

        self.image = load_image('image//Brave_Cookie_Run_Jump_Slide.png')      #이미지 로드
        self.const_x, self.const_y = Cookie_Info['x'], Cookie_Info['y']
        self.x , self.y = self.const_x, self.const_y      #그려줄 좌표 초기화
        self.frame = 0      #프레임 값.
        self.total_frames = 0.0
        self.Control_motion = self.STATE_RUN

        self.Change_Y = 0
        self.Chang_Y_D = 0
        self.up = True
        self.Jumping = 0
        self.Jump_Height_Once, self.Jump_Height_Twice = 0,0

    def Frame(self, frame_time):
        self.total_frames += Brave_Cookie.FRAMES_PER_ACTION * Brave_Cookie.ACTION_PER_TIME * frame_time
        if self.Control_motion == self.STATE_RUN :
            self.frame = int(self.total_frames) % 3
        elif self.Control_motion == self.STATE_JUMP: #1단 점프일 때
            self.frame = 0
        elif self.Control_motion == self.STATE_DOUBLE_JUMP :
            if self.up == True:
                self.frame = int(self.total_frames) % 4
            else :
                self.frame = 5
        elif self.Control_motion == self.STATE_SLIDE :
            self.frame = int(self.total_frames) % 2


    def Running(self):
        self.Control_motion = self.STATE_RUN
    def Jump(self):
        self.Control_motion = self.STATE_JUMP
    def Slide(self):
        self.Control_motion = self.STATE_SLIDE
    def Jump_Double(self):
        self.Control_motion = self.STATE_DOUBLE_JUMP

    def Jump_Change_Ysize(self, frame_time) :
        #점프 중으로 바뀌었을 때.
        self.Jump_Height_Once = Brave_Cookie.SCROLL_SPEED_PPS*frame_time * 10
        self.Jump_Height_Twice = Brave_Cookie.SCROLL_SPEED_PPS*frame_time * 10

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

    def get_bb(self):
        if self.Control_motion == self.STATE_RUN:
            return self.x - 60, self.y - 67.5, self.x +60, self.y + 67.5
        elif self.Control_motion == self.STATE_JUMP or self.Control_motion == self.STATE_DOUBLE_JUMP:
            return self.x - 70, self.y - 82.5, self.x +70, self.y + 82.5
        elif self.Control_motion == self.STATE_SLIDE :
            return self.x - 85, self.y - 40 - 40, self.x +85, self.y + 40 - 40

    def Cookie_HitBox_On(self):
        draw_rectangle(*self.get_bb())