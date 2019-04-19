import pygame,sys
from Statement import Statement


class window():
    
    def __init__(self,screen_size,name='My program'):
        pygame.init()
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(name)
        self._button = []
    @property
    def getSizeScreen(self):
        return self.screen_size
    @property
    def refresh(self):
        pygame.display.update()
        
    def background_color(self,color):
        self.screen.fill(color)
        
    def blit(self,img,polozenie):
        self.screen.blit(img,(polozenie[0],polozenie[1]))
    
    def button(self,img,function,polozenie,tekst="unknown",xy=(15,8)):
        self._button.append(Button(img,function,polozenie,self,tekst,xy))
    

    

class Button:
    def __init__(self,img,function=None,polozenie=(15,15),window=None,napis="unknown",xy=(15,8)):
        self.img =  pygame.image.load('img/'+img+'.png')
        self.pos = polozenie
        self.xy=xy
        #Sself.rect = self.img.get_rect()
        self.napis = napis
        self.window=window
        if function == None:
            self._funtions={}
        else:
            self._funtions = function

        
    def blit(self,color):
        self.window.screen.blit(self.img,(self.pos[0],self.pos[1]))
        tekst=Statement(self.napis,"Verdena",20,color)
        self.window.screen.blit(tekst.draw,(self.pos[0]+self.xy[0],self.pos[1]+self.xy[1]))

    @property
    def functions(self):
        return self._funtions
    @functions.setter
    def functions(self,new_functions):
        if isinstance(new_functions,dict):
            if len(new_functions)==1:
                self._funtions=new_functions
            else:
                print("Przycisk może posiadać tylko jedną funkcję ;), przycisk został zresetowany i nie posiada żadnej funkckcji")
                self._funtions={}
        else:
            print("Funkcja przyciysku musi być podana jako słownik, utworzono pusty słownik")
            self._funtions={}
        
        
if __name__ == "__main__":
    lev=window((800,600))
    lev.background_color([100,100,100])
    lev.refresh
    #tekst=Statement("Game","Verdena",20,(0,0,255))
    #print(tekst.draw)
    lev.button("button",(245,237),"Start",(30,8))
    #lev.blit(tekst.draw,[245,237])
    lev.refresh
