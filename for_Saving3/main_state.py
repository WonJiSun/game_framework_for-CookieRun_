import random
import json
import os

from pico2d import *

import game_framework
import title_state
import BraveCookie_Object
import Scrolling


name = "MainState"

braveCookie = None
Back_Ground = None
Back_Ground2 = None
running = True
Sliding = 0
Jumping = 0

PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global braveCookie
    global Back_Ground
    global Back_Ground2
    braveCookie = BraveCookie_Object.Brave_Cookie()
    Back_Ground = Scrolling.Background(1136,640)
    Back_Ground2 = Scrolling.Background2(1136,640)


def exit():
    global braveCookie
    global Back_Ground
    del(braveCookie)
    del(Back_Ground)
    del(Back_Ground2)

def pause():
    pass


def resume():
    pass


def handle_events():
    global running      #함수가 작동 중인지 여부 확인.

    global Sliding      # 슬라이딩 중 다른 조작 못 하게.
    global Jumping      # 점프 중 다른 조작 못 하게.

    global braveCookie
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT :     #나가기 버튼을 누르면 함수 종료.
            game_framework.quit()
        elif event.type == SDL_KEYDOWN: #키 다운 상태일 때.
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_UP :
                if braveCookie.Jumping == 0:
                    braveCookie.Jump()
                    braveCookie.PlusJumping()
                elif braveCookie.Jumping == 1:
                    braveCookie.ReDifine_Frame()
                    braveCookie.Jump_Double()
            elif event.key == SDLK_DOWN and braveCookie.Jumping == 0:
                braveCookie.Slide()
                Sliding += 1
        if event.type == SDL_KEYUP :    #키를 떼면!
            if Sliding != 0 :
                braveCookie.Running()
                Sliding = 0


def update():
    current_time = get_time()
    frame_time =get_frame_time()
    Back_Ground.update(frame_time)
    Back_Ground2.update(frame_time)
    braveCookie.Frame(frame_time)
    braveCookie.Jump_Change_Ysize(frame_time)

def draw():
    clear_canvas()
    Back_Ground.draw()
    Back_Ground2.draw()
    braveCookie.draw()

    Back_Ground.Timer_Now()
    Back_Ground2.Timer_Now()

    update_canvas()




