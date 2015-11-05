import random
import json
import os

from pico2d import *

import game_framework
import title_state
import BraveCookie_Object



name = "MainState"

braveCookie = None
running = True
Sliding = 0
Jumping = 0


def enter():
    global braveCookie
    braveCookie = BraveCookie_Object.Brave_Cookie()


def exit():
    global braveCookie
    del(braveCookie)


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
    braveCookie.Frame()
    braveCookie.Jump_Change_Ysize()


def draw():
    clear_canvas()
    braveCookie.draw()
    update_canvas()

    delay(0.08)




