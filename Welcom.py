import pygame,sys
from window_configure import window
from design import color
from Statement import Statement
from run2 import Game

        
class Welcom:
    def __init__(self,size=(800,600),nameWindow='My game'):
        self.size=size
        pygame.init()
        self.screen=window(self.size,nameWindow)
        
        
        self.game=Game(self.screen)

        self.screen.button("button",{"Start":self.game.gameLoop},(650,200),"Start",(30,8))
        self.screen.button("button",{"Exit":sys.exit},(650,250),"Exit",(30,8))
        self.option = 0
        self.arrow = None
        
        self.start_program()
        
        
    def start_program(self):
        self.arrow=Arrow((self.screen._button[self.option].pos[0]-75,self.screen._button[self.option].pos[1]-10),self) 
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_w:
                    if self.option >= 0:
                        self.option -= 1
                        self.arrow.polezenie = (self.screen._button[self.option].pos[0]-75,self.screen._button[self.option].pos[1]-10)
                        
                    elif self.option == 0:
                        self.option = len(self.screen._button)
                        self.arrow.polezenie = (self.screen._button[self.option].pos[0]-75,self.screen._button[self.option].pos[1]-10)

                        
                    else:
                        self.option=0
                        self.arrow.polezenie = (self.screen._button[self.option].pos[0]-75,self.screen._button[self.option].pos[1]-10)
                        
                        
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_s:
                    if self.option < len(self.screen._button)-1:
                        self.option += 1
                        self.arrow.polezenie = (self.screen._button[self.option].pos[0]-75,self.screen._button[self.option].pos[1]-10)
                        
                    else:
                        self.option=0
                        self.arrow.polezenie = (self.screen._button[self.option].pos[0]-75,self.screen._button[self.option].pos[1]-10)
                        
                        
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    self.use_function()
            self.tick()
            self.screen.refresh

    def tick(self):
        self.screen.background_color(color.aliceblue())
        self.screen._button[0].blit(color.white())
        self.screen._button[1].blit(color.white())
        self.arrow.blit_arrow()
    def use_function(self):
        if self.option == 0:
            self.screen._button[self.option].functions.get("Start")(self.game.number_level)
        if self.option == 1:
            self.screen._button[self.option].functions.get("Exit")()
        
    
        
class Arrow(pygame.sprite.Sprite):
    def __init__(self,pos,window):
        super().__init__()
        self.screen = window.screen
        self.img=pygame.image.load('img/arrow.png')
        self.pos=pos
        #rect=self.img.get_rect(x=self.pos[0],y=self.pos[1])
        self.blit_arrow()
        

    def blit_arrow(self):
        #self.kill()
        self.screen.blit(self.img, self.pos)
        
    @property
    def polozenie(self):
        return self.pos
    @polozenie.setter
    def polezenie(self,new_polozenie):
        self.pos=new_polozenie
        
    
    
        
        

    
        
if __name__ == "__main__":
    Welcom()
        
        
                
        
       
    
