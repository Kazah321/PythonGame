import pygame
class Statement:
    def __init__(self,text,czcionka,size,color):
        self.czcionka=pygame.font.SysFont(czcionka,size)
        self.text=text
        self.render_text=self.text_render(color)
        
    def text_render(self,color):
        return self.czcionka.render(self.text,True,color)
    @property
    def draw(self):
        return self.render_text
