__author__ = 'rowell'

from pico2d import *
import Collision

class Jelly:
    #1번의 속도
    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, x, y):
        self.image = load_image('image//Jelly.png') # backG_stage1_1.png
        self.speed = Jelly.SCROLL_SPEED_PPS
        self.locateX = x
        self.locateY = y

    def draw(self): #그려주는 함수.
        self.image.clip_draw(0, 0 ,60 ,50 , self.locateX , self.locateY)

    def update(self, frame_time): #조절
        self.locateX = (self.locateX - frame_time * self.speed)

    def get_bb(self):
        return self.locateX - 30 , self.locateY - 25 , self.locateX + 30 , self.locateY + 25

    def Jelly_HitBox_On(self):
        draw_rectangle(*self.get_bb())