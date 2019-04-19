import pygame
from levels import levels
from charcter import Cat,Ghost
from pygame.math import Vector2



class Board:
    def __init__(self,level):
        #self.player=player
        self.walls = []
        self.cheeses = []
        self.traps = []
        self.enemy = []
        self.doors=[]
        self.trigers=[]
        self.door_with_triger = 0
        self.lev = levels()
        self.next_level = None
        self.positon_of_gamer = [168, 245]
        self.create_board(level)
        self.next_level.Update_cheese(len(self.cheeses))

        
        
        
    def create_board(self,k):
        x= y = 0
        self.mapa=self.lev.get_level[k]
        for row in self.mapa:
            for col in row:
                if col =="X":
                    self.walls.append(Wall((x,y)))
                if col =="x":
                    self.walls.append(Wall((x,y),"GhostWall"))
                if col =="E":
                    self.next_level=Winlevel((x,y))
                if col =="C":
                    self.cheeses.append(Cheese((x,y)))
                if col =="T":
                    self.traps.append(Trap((x,y)))
                if col =="c":
                    self.enemy.append(Cat((x,y)))
                if col =="g":
                    self.enemy.append(Ghost((x,y)))
                if col =="G":
                    self.positon_of_gamer =[x,y]
                if col =="D":
                    self.doors.append(Door((x,y),"xy"))
                if col =="d":
                    self.doors.append(Door((x,y),"yx"))
                if col =="t":
                    self.trigers.append(Doors_triger((x,y),self.doors[self.door_with_triger]))
                    self.door_with_triger+=1
                    
                    
                x += 40
            y += 30
            x = 0
        
    
    def game(self,game):
        self.game=game
    def wall(self):
        return self.walls
    def nextLevel(self):# return object WinLevel
        return self.next_level
##    def player(self,player):
##        self.player=player
##        

class Wall:
    def __init__(self,pos,typeOfWall=None):
        if typeOfWall==None:
            self.typeWall=None
            self.ImgWall= pygame.image.load('img/wall.png')
        if typeOfWall == "GhostWall":
            self.ImgWall= pygame.image.load('img/wall2.png')
            self.typeWall="GhostWall"
        self.rect = self.ImgWall.get_rect(topleft=pos)
        self.pos = Vector2(pos[0],pos[1])

    def sprawdz(self):
        if self.typeWall == "GhostWall":
            return True
        else:
            return False
    
        
                
class Winlevel:
    def __init__(self,position):
        self.my_exit=pygame.image.load('img/door.png')
        self.pos=Vector2(position[0],position[1])
        self.rect=self.my_exit.get_rect(topleft=self.pos)
        self.cheese =0
        self.you_can_go=False

    def If_win(self):
        if self.cheese<=0:
            self.my_exit=pygame.image.load('img/door_open.png')
            self.you_can_go=True
            
    def Update_cheese(self,number):
        self.cheese=number
    def take_cheese(self):
        self.cheese-=1
    
            
        
class Cheese:
    def __init__(self,position):
        self.img_cheese=pygame.image.load('img/cheese.png')
        self.pos=Vector2(position[0],position[1])
        self.rect=self.img_cheese.get_rect(topleft=self.pos)
class Trap:
    def __init__(self,position):
        self.img_trap=pygame.image.load('img/pulapka_pusta.png')
        self.pos=Vector2(position[0],position[1])
        self.rect=self.img_trap.get_rect(topleft=self.pos)

    def kill(self):
        self.img_trap=img_trap=pygame.image.load('img/pulapka_pelna.png')

class Door:
    def __init__(self,position,x="xy"):
        self.x=x
        if self.x=="xy":
            self.img_door=pygame.image.load('img/door_wall.png')
        else:
            self.img_door=pygame.image.load('img/door_wall_yx.png')
            
        self.pos=Vector2(position[0],position[1])
        self.rect=self.img_door.get_rect(topleft=self.pos)
        self.collision = True
    def open(self):
        if self.x=="xy":
            self.img_door=pygame.image.load('img/door_wall_open.png')
        else:
            self.img_door=pygame.image.load('img/door_wall_yx_open.png')
        self.collision = False
        
class Doors_triger:
    def __init__(self,position,door):
        self.door=door
        self.collision = True
        self.img_door=pygame.image.load('img/door_triger_off.png')
        self.pos=Vector2(position[0],position[1])
        self.rect=self.img_door.get_rect(topleft=self.pos)
        
        
            
    def action(self):
        self.img_door=pygame.image.load('img/door_triger_on.png')
        self.door.open()
        self.collision = False
            
        

        
        
    
    
    
if __name__ == "__main__":
    lev=Board(2)
    
