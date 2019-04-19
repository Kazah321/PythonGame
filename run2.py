import pygame,sys
from window_configure import window
from design import color
from gracz3 import gracz
from boards import Board,Wall,Winlevel,Trap
from Statement import Statement

        
class Game:
    def __init__(self,screen):
        # Config
        self.tps = 60.00
        
        # Initialization
        pygame.init()
        self.screen=screen
        self._clock = pygame.time.Clock()
        self._delta = 0.0

        self.If_not_next = True
        self.win = None
        self.txt = None
        self.number_level = 0
        
        self.lev=Board(self.number_level)
        for enemy in self.lev.enemy:
            enemy.take_level(self.lev)
        self.End=True
        self.player=gracz(self)
        
        
        
    def gameLoop(self,number_level=0):
        while self.End:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            # Ticking
            self._delta += self._clock.tick() /1000
            while self._delta > 1 / self.tps:
                self.tick()
                self._delta -= 1 / self.tps

            if self.If_not_next:
                self.screen.background_color(color.lightsteelblue())
                self.level(number_level)
                self.draw()
                if self.txt !=None:
                    x,y=self.screen.getSizeScreen
                    self.screen.blit(self.txt,[x/2,y/2])
                if self.End:
                    self.screen.refresh

            else:
                self.number_level +=1
                self.level(self.number_level,True)
                self.If_not_next=True

        # del(self.player)
        self.screen.refresh
    
                    
        
    def tick(self):
        self.player.tick()
        for enemy in self.lev.enemy:
            enemy.tick()
        #self.lev.player(self.player)
    def draw(self):
        self.player.draw()
        for enemy in self.lev.enemy:
            image, polozenie=enemy.draw()
            self.screen.blit(image, polozenie)
        
    def level(self,number_of_level, nextlevel =False):
        if(nextlevel):
            self.lev = Board(number_of_level)
        for wall in self.lev.walls:
            self.screen.blit(wall.ImgWall,[wall.pos.x, wall.pos.y])
        self.win=self.lev.nextLevel()
        self.screen.blit(self.win.my_exit,[self.win.pos.x, self.win.pos.y])
        
        for cheese in self.lev.cheeses:
            self.screen.blit(cheese.img_cheese, [cheese.pos.x, cheese.pos.y])
        for trap in self.lev.traps:
            self.screen.blit(trap.img_trap, [trap.pos.x, trap.pos.y])
        for door in self.lev.doors:
            self.screen.blit(door.img_door, [door.pos.x, door.pos.y])
        for triger in self.lev.trigers:
            self.screen.blit(triger.img_door, [triger.pos.x, triger.pos.y])
        for enemy in self.lev.enemy:
            enemy.take_level(self.lev)

        self.player.update_level(self.lev,self.win,self.lev.positon_of_gamer)
        
            
    def next_level(self):
        self.If_not_next=False
        
    def player_death(self):
        tekst = Statement("GAME OVER!","Verdena",50,(0,0,0))
        # print(self.screen.getSizeScreen)
        self.txt = tekst.draw
        self.screen.refresh
        self.End = False
        
       

if __name__== "__main__":
    Game()

