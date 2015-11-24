import random
import json
import os

import game_framework
import title_state
import MapEditor_Tile_Class

name = "MapEditState"
image = None
imageSize = [1136, 640]

from pico2d import *

Tile = None

def enter():
    global Tile
    Tile = MapEditor_Tile_Class.Map_tile()


def exit():
    global Tile
    del(Tile)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT :
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)

def update():
    pass


def draw():
    clear_canvas()
    Tile.draw()
    update_canvas()

    delay(0.08) #속도 결정.