__author__ = 'rowell'

from pico2d import *

Default_Size = [60,320]
imageSize = [1136, 640]

class Map_tile:
    def __init__(self):
        self.image_Editor_Default = load_image('Map_Editor.png')      #이미지 로드
        self.image_Editor_DownOb1 = load_image('Map_Editor_DownObject.png')
        self.image_Editor_DownOb2 = load_image('Map_Editor_DownObject_S.png')
        self.image_Editor_Up = load_image('Map_Editor_Hole.png')

        self.x , self.y = 1136/2,640/2     #그려줄 좌표 초기화
    def draw(self):
            self.image_Editor_Default.clip_draw(0, 0 ,60 ,320 , self.x , self.y)