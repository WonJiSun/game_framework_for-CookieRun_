import game_framework
import main_state
import Map_Edit_State
from pico2d import *


name = "TitleState"
image = None
imageSize = [1136, 640]


def enter():
    global image
    image = load_image('Title_cookie.png')


def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(Map_Edit_State)



def draw():
    clear_canvas()
    image.draw(imageSize[0]/2,imageSize[1]/2)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






