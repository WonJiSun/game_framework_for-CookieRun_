__author__ = 'rowell'

from pico2d import *

class Background:
    #1번의 속도
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.image = load_image('image//backG_stage1_1.png') # backG_stage1_1.png
        self.speed = Background.SCROLL_SPEED_PPS
        self.left = 0
        self.screen_width = w
        self.screen_height = h
        self.current_time = 0
        self.Changed_stage2 = False

    def draw(self):
        #left botton width height x y
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0 , w ,self.screen_height , 0 ,0)
        self.image.clip_draw_to_origin(0, 0 , self.screen_width -w,self.screen_height , w ,0)


    def update(self, frame_time):
        self.left = (self.left + frame_time *self.speed) % self.image.w

    def Timer_Now(self):
        self.current_time = get_time()
        if(self.current_time > 20) :
            if self.Changed_stage2 == False :
                self.image = load_image('image//backG_stage2_1.png')
                self.Changed_stage2 = True



class Background2:
    #2번의 속도
    PIXEL_PER_METER2 = (10.0 / 0.15)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH2 = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM2 = (SCROLL_SPEED_KMPH2 * 1000.0 / 60.0)
    SCROLL_SPEED_MPS2 = (SCROLL_SPEED_MPM2 / 60.0)
    SCROLL_SPEED_PPS2 = (SCROLL_SPEED_MPS2 * PIXEL_PER_METER2)

    def __init__(self, w, h):
        self.image = load_image('image//backG_stage1_2.png') # backG_stage1_1.png
        self.speed = Background2.SCROLL_SPEED_PPS2
        self.left = 0
        self.screen_width = w
        self.screen_height = h
        self.current_time = 0
        self.Changed_stage2 = False

    def draw(self):
        #left botton width height x y
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0 , w ,self.screen_height , 0 ,0)
        self.image.clip_draw_to_origin(0, 0 , self.screen_width -w,self.screen_height , w ,0)


    def update(self, frame_time):
        self.left = (self.left + frame_time *self.speed) % self.image.w

    def Timer_Now(self):
        self.current_time = get_time()
        if(self.current_time > 20) :
            if self.Changed_stage2 == False :
                self.image = load_image('image//backG_stage2_4.png')
                self.Changed_stage2 = True